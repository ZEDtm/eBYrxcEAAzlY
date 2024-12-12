from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.callback_factory import MenuCallbackData, BackCallbackData, \
    SupportCallbackData, Account, ServiceCallback


async def get_lk_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    markup.button(
        text='Личный кабинет',
        callback_data=MenuCallbackData(
            lk=True
        )
    )

    markup.button(
        text='Отчет',
        callback_data=MenuCallbackData(
            report=True
        )
    )

    markup.button(
        text='Поддержка',
        url='https://t.me/investpotok_help'
    )

    markup.button(
        text='Хочу купить оборудование',
        callback_data=MenuCallbackData(
            buy=True
        )
    )

    markup.button(
        text='Хочу продать оборудование',
        callback_data=MenuCallbackData(
            sell=True
        )
    )

    markup.button(
        text='Услуги предоставляет',
        callback_data=ServiceCallback()
    )

    markup.button(
        text='Договор оферты',
        callback_data=MenuCallbackData(
            dogovor=True
        )
    )




    markup.adjust(1)

    return markup.as_markup()


async def back_help_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    markup.button(
        text='Назад',
        callback_data=BackCallbackData(
            help=True
        )
    )

    markup.adjust(1)

    return markup.as_markup()


async def payment_buttons(url: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    markup.button(
        text='Оплатить',
        url=url
    )

    markup.adjust(1)

    return markup.as_markup()


async def get_support_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    markup.button(
        text='Написать',
        url='https://t.me/investpotok_help'
    )
    markup.button(
        text='Позвонить',
        callback_data=SupportCallbackData(
            call=True
        )
    )
    markup.button(
        text='Назад',
        callback_data=BackCallbackData(
            start=True
        )
    )

    markup.adjust(2)

    return markup.as_markup(resize_keyboard=True)


async def get_back_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()


    markup.button(
        text='Назад',
        callback_data=BackCallbackData(
            start=True
        )
    )

    markup.adjust(2)

    return markup.as_markup(resize_keyboard=True)


async def ok_account_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardBuilder()

    markup.button(
        text='Согласовать',
        callback_data=Account(
            yes=True
        )
    )

    markup.button(
        text='Внести правки',
        callback_data=Account(
            no=True
        )
    )

    markup.adjust(1)

    return markup.as_markup()
