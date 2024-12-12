import textwrap
from datetime import datetime, timedelta

import pytz
from aiogram import Bot
from aiogram import types, Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, BufferedInputFile
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from admin_panel.models import TgUser, Report, WorkerUser, ApplicationsBuy, ApplicationsSell
from bot.api_via_btc import get_hash_rate, get_balance
from bot.callback_factory import MenuCallbackData, BackCallbackData, \
    SupportCallbackData, Account
from bot.callback_factory import ServiceCallback
from bot.create_pay import create_pay_iokassa, create_pay_first_iokassa
from bot.create_pdf import create_pdf_uniq_code
from bot.get_now_month import month_name_to_number
from bot.keyboards.inline import get_lk_buttons, payment_buttons, get_support_buttons, back_help_buttons, \
    get_back_buttons, ok_account_buttons
from bot.middleware.apchendler import recurment_pay
from bot.service_async import get_xlsx
from bot.state_group import UserStart

start_router = Router(name=__name__)


@start_router.message(CommandStart())
async def command_start(message: types.Message, state: FSMContext):
    """Команда /start"""
    try:
        code = message.text.split(' ')[1].rstrip()
    except IndexError:
        code = ''

    user: TgUser = await TgUser.objects.filter(
        ref_code=code
    ).afirst()
    document = FSInputFile("Инвест договор оферта.pdf", filename="Договор оферта.pdf")
    await message.answer(

        text=textwrap.dedent(
            '''Индивидуальный предприниматель Холин Сергей Сергеевич 
 
ИНН: 
524613254304 
 
ОГРНИП: 324527500068927

Цены на товар: Оплата товара складывается исходя из количества оборудования, которое имеет пользователь, по формуле:

900 х (количество оборудования)

Способы оплаты: В боте доступная оплата безналичными (списание с карты)

Условия возврата: Условия возврата обговаривается индивидуально через поддержку в боте

Чтобы связаться с поддержкой, необходимо нажать на одноименную кнопку «поддержка» в боте и описать свой запрос

Политика конфиденциальности и соглашение на обработку персональных данных предсмутрена самим сервисом телеграм

Принципы конфиденциальности

В вопросах сбора и обработки персональных данных Telegram придерживается двух основополагающих принципов:

1) Мы не используем данные Вашей переписки для показа рекламы.
2) Мы храним только те данные, которые необходимы для корректной работы Telegram в качестве надёжного и многофункционального сервиса для обмена сообщениями.

Ознакомиться с ними можно по ссылке:

Политика конфиденциальности:
- <a href="https://telegram.org/privacy/ru#2-pravovie-osnovaniya-dlya-obrabotki-personalnih-dannih">На каких правовых основаниях мы обрабатываем персональные данные</a>
- <a href="https://telegram.org/privacy/ru#3-vidi-personalnih-dannih-kotorie-mi-ispolzuem">Какие из Ваших персональных данных мы можем собирать</a>
- <a href="https://telegram.org/privacy/ru#4-bezopasnost-personalnih-dannih">Как мы обеспечиваем безопасность персональных данных</a>
- <a href="https://telegram.org/privacy/ru#5-obrabotka-personalnih-dannih">Для каких целей мы можем использовать персональные данные</a>       
- <a href="https://telegram.org/privacy/ru#8-litsa-kotorim-mogut-bit-peredani-vashi-personalnie-dannie">Кому могут быть переданы персональные данные</a>
- <a href="https://telegram.org/privacy/ru#9-vashi-prava-v-otnoshenii-predostavlennih-personalnih-dannih">Какие у Вас есть права в отношении Ваших персональных данных</a>
Пользовательское соглашение: https://telegram.org/tos/ru
'''),
        parse_mode='HTML'
    )
    await message.answer_document(
        caption=textwrap.dedent(
            'Можете ознакомится с договором'
        ),
        document=document
    )
    await state.clear()
    await state.update_data({})
    await state.set_state(UserStart.start)

    if user:
        if user.telegram_id:
            await state.update_data({})
            await message.answer(
                'Меню',
                reply_markup=await get_lk_buttons()
            )

        else:
            user.telegram_id = message.from_user.id
            user.username = message.from_user.username
            await user.asave()
            await message.answer(
                textwrap.dedent(
                    '''
Рады приветствовать вас в сервис боте «InvestMi». 
Для того, чтобы мы начали управлять вашим оборудованием,
нам необходимо составить и подписать договор управления.
Ответьте пожалуйста на ряд вопросов, ответы на которые автоматически подгрузятся в договор. 
'''
                )
            )
            await message.answer(
                textwrap.dedent(
                    '''
Введите ваши паспортные данные (серия, номер) 
Пример: 1234 123123
'''
                )
            )
            await state.set_state(UserStart.send_passport)
    else:
        user: TgUser = await TgUser.objects.filter(
            telegram_id=message.from_user.id
        ).afirst()

        if user:
            if user.status_asccount:
                await message.answer(
                    'Меню',
                    reply_markup=await get_lk_buttons()
                )
            else:
                if user.bank_name:
                    return await message.answer(
                        'Ваш аккаунт на рассмотрении'
                    )
                await message.answer(
                    textwrap.dedent(
                        '''
Рады приветствовать вас в сервис боте «InvestMi». 
Для того, чтобы мы начали управлять вашим оборудованием,
нам необходимо составить и подписать договор управления.
Ответьте пожалуйста на ряд вопросов, ответы на которые автоматически подгрузятся в договор. 
'''
                    )
                )
                await state.set_state(UserStart.send_passport)
                await message.answer(
                    textwrap.dedent(
                        '''
Введите ваши паспортные данные (серия, номер) 
Пример: 1234 123123
'''
                    )
                )


@start_router.message(UserStart.send_passport)
async def get_passport(message: Message, state: FSMContext):
    passport_data = message.text

    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.passport = passport_data
    await user.asave()

    await state.set_state(UserStart.passport_get)

    await message.answer(
        textwrap.dedent(
            '''
Введите кем выдан паспорт 
Пример: ГУ МВД РОССИИ ПО Г.МОСКВЕ 
'''
        )
    )


@start_router.message(UserStart.passport_get)
async def get_passport_get(message: Message, state: FSMContext):
    passport_get = message.text
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.get_passport = passport_get
    await user.asave()

    await state.set_state(UserStart.passport_date)

    await message.answer(
        textwrap.dedent(
            '''
Введите дату выдачи паспорта 
Пример: 01.07.1999
'''
        )
    )


@start_router.message(UserStart.passport_date)
async def get_passport_date(message: Message, state: FSMContext):
    passport_date = message.text
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.date_passport = passport_date
    await user.asave()

    await state.set_state(UserStart.address_registration)

    await message.answer(
        textwrap.dedent(
            '''
Введите адрес регистрации
Пример: г.Москва, ул. Ленина, д.1, кв.5
'''
        )
    )


@start_router.message(UserStart.address_registration)
async def get_address_registration(message: Message, state: FSMContext):
    address_registration = message.text
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.address_registration = address_registration
    await user.asave()

    await state.set_state(UserStart.send_bic)

    await message.answer(
        textwrap.dedent(
            '''
Введите БИК вашего банка 
Пример: 044525974
'''
        )
    )


@start_router.message(UserStart.send_bic)
async def get_passport(message: Message, state: FSMContext):
    bic = message.text
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.bank_bik = bic
    await user.asave()

    await state.set_state(UserStart.send_correspondent)

    await message.answer(
        textwrap.dedent(
            '''
Введите корр. счет 
Пример: 30101810145250000974
'''
        )
    )


@start_router.message(UserStart.send_correspondent)
async def get_passport(message: Message, state: FSMContext):
    correspondent = message.text
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.corr_account = correspondent

    await user.asave()

    await state.set_state(UserStart.send_bank_name)

    await message.answer(
        textwrap.dedent(
            '''
Введите наименование банка 
Пример: АО «Тинькофф Банк»
'''
        )
    )


@start_router.message(UserStart.send_bank_name)
async def get_number_account(message: Message, state: FSMContext):
    bank_name = message.text
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.bank_name = bank_name
    await user.asave()

    await state.set_state(UserStart.send_number_account)

    # await state.set_state(UserStart.send_number_account)

    await message.answer(
        textwrap.dedent(
            '''
Введите номер вашего счета 
Пример: 40817810100005841440
'''
        )
    )


@start_router.message(UserStart.send_number_account)
async def get_account(message: Message, state: FSMContext):
    number_account = message.text
    # pdf_code = TgUser.generate_pdf_code()
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.number_account = number_account

    await user.asave()

    await state.set_state(UserStart.send_name_worker)

    await message.answer(
        textwrap.dedent(
            '''
Введите серийный номер вашего оборудования по 1 номеру в каждом сообщении 
Пример: HGT304729GO2792F
'''
        )
    )


@start_router.message(UserStart.send_name_worker)
async def get_workers_name(message: Message, state: FSMContext):
    tg_user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    workers_count = await WorkerUser.objects.filter(
        user__telegram_id=message.from_user.id
    ).acount()
    if workers_count != tg_user.workers:
        await WorkerUser.objects.acreate(
            name=message.text,
            user=tg_user
        )
        workers_count = await WorkerUser.objects.filter(
            user__telegram_id=message.from_user.id
        ).acount()
        if workers_count != tg_user.workers:
            await state.set_state(UserStart.send_name_worker)
            workers_count = await WorkerUser.objects.filter(
                user__telegram_id=message.from_user.id
            ).acount()
            return await message.answer(
                textwrap.dedent(
                    f'''
Осталось: {tg_user.workers - workers_count}
'''
                )
            )

    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    await create_pdf_uniq_code(
        tg_user=user
    )

    document = FSInputFile(f"/bot/Агентский договор {message.from_user.id}.pdf",
                           filename=f"Агентский договор №{message.from_user.id}.pdf")
    await message.answer_document(
        document=document,
        caption='Выберите',
        reply_markup=await ok_account_buttons()
    )


@start_router.message(UserStart.send_number_account)
async def get_number_account(message: Message, state: FSMContext, ):
    number_account = message.text
    pdf_code = TgUser.generate_pdf_code()
    user: TgUser = await TgUser.objects.filter(
        telegram_id=message.from_user.id
    ).afirst()

    user.number_account = number_account
    await user.asave()

    await message.answer(
        'Ваш договор подготавливается .......'
    )

    await create_pdf_uniq_code(
        tg_user=user
    )
    await state.set_state(UserStart.send_number_account)

    document = FSInputFile(f"Агентский договор {message.from_user.id}.pdf", filename="Агентский договор.pdf")
    await message.answer_document(
        document=document,
        caption='Выберите',
        reply_markup=await ok_account_buttons()
    )


@start_router.callback_query(Account.filter(F.yes))
async def get_yes(call: CallbackQuery, state: FSMContext, apscheduler: AsyncIOScheduler):
    url, payment_id = await create_pay_iokassa(call.from_user.id)
    await call.message.edit_caption(
        caption=textwrap.dedent(

            '''
для того, чтобы подписать данный договор, вам необходимо перейти в приложение 
<a href="https://lk.nopaper.ru/">Nopapper</a>.

<a href="https://telegra.ph/Kak-ispolzovat-Nopaper-11-21/">Инструкция по работе с приложением Nopapper</a>.
'''
        ),
        parse_mode='HTML',
        reply_markup=await payment_buttons(url)
    )

    time_check = datetime.now(pytz.timezone('Europe/Moscow')).now() + timedelta(days=30)

    await state.set_state(UserStart.wait_pay)
    apscheduler.add_job(
        recurment_pay,
        trigger='interval',
        start_date=time_check,
        days=30,
        replace_existing=True,
        kwargs={
            'telegram_id': call.from_user.id,
        },
        id=f'start_notification_{call.from_user.id}'
    )


@start_router.callback_query(Account.filter(F.no))
async def get_no(call: CallbackQuery, state: FSMContext, apscheduler: AsyncIOScheduler):
    url, payment_id = await create_pay_iokassa(call.from_user.id)
    await call.message.edit_caption(
        caption=textwrap.dedent(
            '''

Мы обязательно внесем правки в ваш договор ,
напишите нам @investpotok_help, какие именно правки необходимо вести

Как только мы увидим что подписан договор и пришла оплата, то сразу дадим доступ
'''
        ),
        reply_markup=await payment_buttons(url)
    )

    time_check = datetime.now(pytz.timezone('Europe/Moscow')).now() + timedelta(days=30)

    await state.set_state(UserStart.wait_pay)
    apscheduler.add_job(
        recurment_pay,
        trigger='interval',
        start_date=time_check,
        days=30,
        replace_existing=True,
        kwargs={
            'telegram_id': call.from_user.id,
        },
        id=f'start_notification_{call.from_user.id}'
    )


@start_router.callback_query(MenuCallbackData.filter(F.lk))
async def get_lk(call: CallbackQuery):
    user: TgUser = await TgUser.objects.filter(telegram_id=call.from_user.id).afirst()
    if not user.api_key:
        await call.answer(
            'Необходимо добавить API ключ',
        )
    answer = ''

    statistic = await get_hash_rate(call.from_user.id)
    balance = await get_balance(call.from_user.id)
    if user.subscribe:
        answer += '\n<b>Общий баланс:</b>'
        for i in balance.data.balance:
            answer += f'\n- {i.amount} {i.coin}\n'

        answer += textwrap.dedent(
            f'''\n\n
            <b>Средний хэшрейт за 10 минут:</b> {int(statistic.data.hashrate_10min) / 1000000000000}
            <b>Средний хэшрейт за час:</b> {int(statistic.data.hashrate_1hour) / 1000000000000}
            <b>Средний хэшрейт за день:</b> {int(statistic.data.hashrate_24hour) / 1000000000000}
            <b>Активные воркер:</b> {statistic.data.active_workers}
            <b>Неактивные воркеры:</b> {statistic.data.unactive_workers}
            '''
        )

    try:
        await call.message.edit_text(
            answer,
            reply_markup=await get_back_buttons(),
            parse_mode='HTML',
        )
    except TelegramBadRequest:
        pass


@start_router.callback_query(MenuCallbackData.filter(F.report))
async def get_report(call: CallbackQuery):
    user: TgUser = await TgUser.objects.filter(telegram_id=call.from_user.id).afirst()

    name, number = month_name_to_number()
    report = await Report.objects.filter(
        month__iexact=name,
        created_at__month=number,
        user__iexact=user.fio,
    ).afirst()
    if not report:
        return call.message.answer(
            '''
Отчет будет приходить вам сообщением ежемесячно с стандартном формате.
После получения отчета, вам будет открыта возможность оплатить электричество рублями
с любым удобным способом.
'''

        )
    if report:
        if user.by_report_month == name:

            file = BufferedInputFile(await get_xlsx(name, number), filename=f'{user.fio}.xlsx')

            await call.message.answer_document(
                document=file
            )
        else:
            url, payment_id = await create_pay_first_iokassa(user.telegram_id, report.pay_main)
            await call.message.answer(
                textwrap.dedent(
                    'Вам необходимо оплатить электричество'
                ),
                reply_markup=await payment_buttons(url)
            )

    else:
        url, payment_id = await create_pay_first_iokassa(user.telegram_id, report.pay_main)
        await call.message.answer(
            textwrap.dedent(
                'Вам необходимо  оплатить электричество'
            ),
            reply_markup=await payment_buttons(url)
        )


##Все свзязанное с разделом поддержка
@start_router.callback_query(MenuCallbackData.filter(F.help))
async def get_help(call: CallbackQuery):
    await call.message.edit_text(
        textwrap.dedent(
            'Выберите способ связи'
        ),
        reply_markup=await get_support_buttons()
    )


@start_router.callback_query(SupportCallbackData.filter(F.write))
async def support_help_write(call: CallbackQuery, bot: Bot):
    await call.message.edit_text(
        textwrap.dedent(
            '@example свяжитесь'
        ),
        reply_markup=await back_help_buttons()
    )


@start_router.callback_query(SupportCallbackData.filter(F.call))
async def support_help_call(call: CallbackQuery, bot: Bot):
    await call.message.edit_text(
        textwrap.dedent(
            '8-800-535-35-35 проще позвонить чем у кого-то занимать'
        ),
        reply_markup=await back_help_buttons()
    )


@start_router.callback_query(BackCallbackData.filter(F.help))
async def get_back_help(call: CallbackQuery):
    await call.message.edit_text(
        textwrap.dedent(
            'Выберите способ связи'
        ),
        reply_markup=await get_support_buttons()
    )


@start_router.callback_query(BackCallbackData.filter(F.start))
async def get_back_menu(call: CallbackQuery):
    await call.message.edit_text(
        textwrap.dedent(
            'Меню'
        ),
        reply_markup=await get_lk_buttons()
    )


@start_router.callback_query(MenuCallbackData.filter(F.buy))
async def buy_tech(call: CallbackQuery):
    user: TgUser = await TgUser.objects.filter(telegram_id=call.from_user.id).afirst()
    await call.answer(
        textwrap.dedent(
            'Ваша заявку на покупку отправлена, с вами обязательно свяжутся'
        ),
    )
    await ApplicationsSell.objects.aget_or_create(
        user=user
    )


@start_router.callback_query(MenuCallbackData.filter(F.sell))
async def sell_tech(call: CallbackQuery):
    user: TgUser = await TgUser.objects.filter(telegram_id=call.from_user.id).afirst()
    await call.answer(
        textwrap.dedent(
            'Ваша заявку на продажу отправлена, с вами обязательно свяжутся'
        ),
    )
    await ApplicationsBuy.objects.aget_or_create(
        user=user
    )


@start_router.callback_query(MenuCallbackData.filter(F.dogovor))
async def get_dogovor(call: CallbackQuery):
    user: TgUser = await TgUser.objects.filter(telegram_id=call.from_user.id).afirst()

    document = FSInputFile(f"Инвест договор оферта.pdf",
                           filename=f"Договор оферта.pdf")
    await call.message.answer_document(
        caption=textwrap.dedent(
            'Можете ознакомится с договором'
        ),
        document=document
    )

    await ApplicationsBuy.objects.aget_or_create(
        user=user
    )


@start_router.callback_query(ServiceCallback.filter())
async def get_service_info(call: CallbackQuery):
    await call.message.edit_text(
        text=textwrap.dedent(
            '''
Индивидуальный предприниматель Холин Сергей Сергеевич 
 
ИНН: 
524613254304 
 
ОГРНИП: 324527500068927

Цены на товар: Оплата товара складывается исходя из количества оборудования, которое имеет пользователь, по формуле:

900 х (количество оборудования)

Способы оплаты: В боте доступная оплата безналичными (списание с карты)

Условия возврата: Условия возврата обговаривается индивидуально через поддержку в боте

Чтобы связаться с поддержкой, необходимо нажать на одноименную кнопку «поддержка» в боте и описать свой запрос

Политика конфиденциальности и соглашение на обработку персональных данных предсмутрена самим сервисом телеграм

Принципы конфиденциальности

В вопросах сбора и обработки персональных данных Telegram придерживается двух основополагающих принципов:

1) Мы не используем данные Вашей переписки для показа рекламы.
2) Мы храним только те данные, которые необходимы для корректной работы Telegram в качестве надёжного и многофункционального сервиса для обмена сообщениями.

Ознакомиться с ними можно по ссылке:

Политика конфиденциальности:
- <a href="https://telegram.org/privacy/ru#2-pravovie-osnovaniya-dlya-obrabotki-personalnih-dannih">На каких правовых основаниях мы обрабатываем персональные данные</a>
- <a href="https://telegram.org/privacy/ru#3-vidi-personalnih-dannih-kotorie-mi-ispolzuem">Какие из Ваших персональных данных мы можем собирать</a>
- <a href="https://telegram.org/privacy/ru#4-bezopasnost-personalnih-dannih">Как мы обеспечиваем безопасность персональных данных</a>
- <a href="https://telegram.org/privacy/ru#5-obrabotka-personalnih-dannih">Для каких целей мы можем использовать персональные данные</a>
- <a href="https://telegram.org/privacy/ru#8-litsa-kotorim-mogut-bit-peredani-vashi-personalnie-dannie">Кому могут быть переданы персональные данные</a>
- <a href="https://telegram.org/privacy/ru#9-vashi-prava-v-otnoshenii-predostavlennih-personalnih-dannih">Какие у Вас есть права в отношении Ваших персональных данных</a>
Пользовательское соглашение: https://telegram.org/tos/ru
'''
        ),
        reply_markup=await get_back_buttons(),
        parse_mode="HTML"
    )
