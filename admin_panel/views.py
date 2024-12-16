# Create your views here.
import asyncio
import json
from datetime import datetime, timedelta
from io import BytesIO
from pprint import pprint
import requests as req
import pytz
from aiogram import Bot
from aiogram.types import BufferedInputFile
from asgiref.sync import sync_to_async
from django.conf import settings
from django.http import HttpResponseForbidden
from bot.get_now_month import month_name_to_number
from bot.misc.mailing import send_message_mailing
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from loguru import logger
from pydantic import BaseModel, ValidationError
from django.http import JsonResponse
from admin_panel.forms import MailingForm
from admin_panel.models import Mailing, TgUser, Admin
from bot.service_async import get_all_admins_id
from bot.yookassa_schema import YooKassaSchema

class WebHookSchema(BaseModel):
    id: str
    status: str
    amount: int
    merchant_transaction_id: str


# Create your views here.
@login_required
def mailing(request):
    if request.method == 'POST':
        form = MailingForm(request.POST, request.FILES)
        if not form.is_valid():
            for error in form.errors.values():
                messages.error(request, error.data[0].message)
            return redirect("admin:admin_panel_mailing_add")
        data = form.cleaned_data
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        file_id = loop.run_until_complete(get_file_id(data.get('file')))
        if file_id == -1:
            messages.error(request, "Неверный формат файла или отсутсвуют администраторы")
            return redirect("admin:admin_panel_mailing_add")
        if data.get('schedule_checkbox'):
            date_malling = data.get('schedule_datetime')
            text_success = 'Рассылка успешно зарегистрирована'
        else:
            date_malling = timezone.now()
            text_success = 'Рассылка успешно зарегистрирована и будет запущена в течении 1 минуты.'

        mailing = Mailing.objects.create(
            media_type=data['media_type'],
            text=data['message_text'],
            date_malling=date_malling,
            file_id=file_id
        )
        if group := data.get('group'):
            mailing.group.set(
                group
            )

        messages.success(request, text_success)
    return redirect("admin:admin_panel_mailing_changelist")


async def get_file_id(file):
    if not file:
        return None
    file_type = file.content_type.split('/')[0]

    if isinstance(file.file, BytesIO):
        file_input = BufferedInputFile(file.file.getvalue(), filename=file.name)
    else:
        bytes_file = BytesIO(file.read())
        file_input = BufferedInputFile(bytes_file.getvalue(), filename=file.name)

    bot = Bot(token=settings.TG_TOKEN_BOT, parse_mode='HTML')
    file_id = -1

    admins = await get_all_admins_id()

    if len(admins) != 0:
        if file_type == 'image':
            message = await bot.send_photo(chat_id=admins[0], photo=file_input)
            file_id = message.photo[-1].file_id
        elif file_type == "video":
            message = await bot.send_video(chat_id=admins[0], video=file_input)
            file_id = message.video.file_id
        else:
            message = await bot.send_document(chat_id=admins[0], document=file_input)
            file_id = message.document.file_id
    return file_id


async def mailing_django(media, text, file_id):
    users = await sync_to_async(TgUser.objects.all)()
    bot = Bot(
        token=settings.TG_TOKEN_BOT,
        parse_mode='HTML'
    )
    count_send = 0
    async for user in users:
        args = [user.telegram_id]
        kwargs = {}
        if media in ['photo', 'video', 'document']:
            args.append(file_id)
            kwargs["caption"] = text
        else:
            args.append(text)
        status = await send_message_mailing(bot, media, args, kwargs)
        if status:
            count_send += 1

    return count_send


@csrf_exempt
def check_pay_view(request):
    if request.method == 'POST':

        response = json.loads(request.body)
        logger.info(response)
        try:
            payment = YooKassaSchema(**response)
        except ValidationError as e:
            logger.critical(e)
            return HttpResponse(status=404)

        user: TgUser = TgUser.objects.filter(telegram_id=payment.object.metadata.telegram_id).first()
        logger.critical(user)
        logger.critical(payment.object.metadata.telegram_id)

        url = f"https://api.telegram.org/bot{settings.TG_TOKEN_BOT}/SendMessage"

        if payment.object.metadata.one_time:

            name, number = month_name_to_number()
            user.by_report_month = name
            user.save()

            try:
                req.post(
                    url, json={
                        'chat_id': user.telegram_id,
                        'text': 'Оплата прошла успешно',
                    })
                return HttpResponse(status=200)

            except Exception as e:
                logger.warning(e)
                return HttpResponse(status=404)


        if payment.object.payment_method.saved:
            user.yookassa_payment_id = payment.object.payment_method.id
            user.subscribe = True
            user.expire_date_subscribe = datetime.now(pytz.timezone('Europe/Moscow')) + timedelta(weeks=4)
            user.save()

            try:
                req.post(
                    url, json={
                    'chat_id': user.telegram_id,
                    'text': 'Оплата прошла успешно',
                })
                return HttpResponse(status=200)
            except Exception as e:
                logger.warning(e)
                return HttpResponse(status=500)
        else:
            user.subscribe = False
            user.yookassa_payment_id = None
            user.save()

            try:
                req.post(
                    url, json={
                        'chat_id': user.telegram_id,
                        'text': 'Оплата не прошла',
                    })
                return HttpResponse(status=200)
            except Exception as e:
                logger.warning(e)
                return HttpResponse(status=500)

        return HttpResponse(status=200)
    return HttpResponse(status=500)


@csrf_exempt
def get_users(request):
    if request.method == 'GET':
        api_key = request.headers.get("Authorization")
        if api_key != "Bearer {}".format('<BOT_TOKEN>'):
            return JsonResponse(
                {"error": "Unauthorized"},
                status=401
            )
        else:
            users = TgUser.objects.all()
            list_users = []
            for user in users:
                if user.telegram_id:
                    list_users.append({'telegram_id': user.telegram_id,
                                       'username': user.username,
                                       'fio': user.fio,
                      'phone': user.phone,
                      'block' :user.block
                    })
            return JsonResponse({'data': list_users}, safe=False)

@csrf_exempt
def get_admin(request):
    if request.method == 'GET':
        api_key = request.headers.get("Authorization")
        if api_key != "Bearer {}".format('<BOT_TOKEN>'):
            return JsonResponse(
                {"error": "Unauthorized"},
                status=401
            )
        else:
            users = Admin.objects.all()
            list_users = []
            for user in users:
                    list_users.append({'telegram_id': user.telegram_id})
            return JsonResponse({'data': list_users}, safe=False)