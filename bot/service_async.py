from datetime import datetime

import pytz
from aiogram.types import User
from asgiref.sync import sync_to_async
from django.db.models import F as Field, F, Q
from loguru import logger

from admin_panel.admin import ReportResource
from admin_panel.models import TgUser, Mailing, Admin, Report, WorkerUser


@sync_to_async
def get_all_users() -> list:
    return list(TgUser.objects.exclude(telegram_id__isnull=True))

@sync_to_async
def get_users_group(group: list) -> list:
    return list(TgUser.objects.filter(group__in=group).exclude(telegram_id__isnull=True))

@sync_to_async
def check_and_update_user(user: User) -> TgUser:
    """Предоставление и обновление модели пользователя"""
    tg_user = TgUser.objects.filter(telegram_id=user.id).first()
    if not tg_user:
        # эти данные могут со временем меняться
        tg_user = TgUser.objects.create(telegram_id=user.id)
        tg_user.telegram_id = user.id
        tg_user.username = user.username
        tg_user.save()
    return tg_user




@sync_to_async
def get_all_maling() -> list:
    now = datetime.now(pytz.timezone('Europe/Moscow'))

    return list(Mailing.objects.filter(is_sent=False, date_malling__lte=now))

@sync_to_async
def get_all_subscribe() -> list:
    now = datetime.now(pytz.timezone('Europe/Moscow'))

    return list(TgUser.objects.filter(expire_date_subscribe__lte=now, subscribe=True))


@sync_to_async
def get_xlsx(month: str, number_month: int) -> bytes | bool:

    queryset = Report.objects.filter(month__iexact=month, created_at__month=number_month)

    dataset = ReportResource().export(queryset=queryset)
    if not queryset:
        return False
    return dataset.xlsx


@sync_to_async
def get_xlsx_user(fio: str, number_month: int = None, month: str = None) -> bytes | bool:
    logger.critical(month)
    logger.critical(number_month)
    logger.critical(fio)
    if month:
        queryset = Report.objects.filter(
            month__iexact=month,
            created_at__month=number_month,
            user__iexact=fio,
        )
        logger.critical(queryset)
    else:
        queryset = Report.objects.filter(
            user__iexact=fio,
        )

    dataset = ReportResource().export(queryset=queryset)
    if not queryset:
        return False
    return dataset.xlsx


@sync_to_async
def get_all_admins_id() -> list:
    return list(Admin.objects.values_list('telegram_id', flat=True))


@sync_to_async
def get_user_workers(user: TgUser) -> list:
    return list(
        WorkerUser.objects.filter(
            user=user
        ).values_list('name', flat=True)
    )