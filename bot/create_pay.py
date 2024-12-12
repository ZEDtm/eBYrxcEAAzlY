
import uuid

from loguru import logger
from yookassa import Configuration, Payment

from admin_panel.models import YookassaConfig, TgUser


async def create_pay_iokassa(user_id: int) -> (str, int):
    """
    Create link for pay Юкасса
    :return: link for pay and id order
    """

    yoocasa_config: YookassaConfig = await YookassaConfig.objects.afirst()
    Configuration.account_id = yoocasa_config.shop_id
    Configuration.secret_key = yoocasa_config.secret_key_yookassa
    logger.critical(user_id)
    idempotence_key = str(uuid.uuid4())
    user: TgUser = await TgUser.objects.filter(telegram_id=user_id).afirst()
    payment = Payment.create({
        "amount": {
            "value": f"{user.workers * user.default_cost}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"{yoocasa_config.bot_url}"
        },
        "capture": True,
        "description": "Вступительный взнос",
        "save_payment_method": True,
        "metadata": {
            "telegram_id": f"{user_id}"
        }
    },

        idempotence_key
    )

    url = payment.confirmation.confirmation_url

    return url, payment.id



async def create_repeat_pay(telegram_id: int):
    """Автоплатеж юкассы"""
    yoocasa_config: YookassaConfig = await YookassaConfig.objects.afirst()
    Configuration.account_id = yoocasa_config.shop_id
    Configuration.secret_key = yoocasa_config.secret_key_yookassa
    user: TgUser = await TgUser.objects.filter(telegram_id=telegram_id).afirst()

    payment = Payment.create({
        "amount": {
            "value": f"{user.workers * user.default_cost}",
            "currency": "RUB"
        },
        "capture": True,
        "payment_method_id": user.yookassa_payment_id,
        "description": "Вступительный взнос",
        "metadata": {
            "telegram_id": f"{telegram_id}"
        }
    })


async def create_pay_first_iokassa(user_id: int, cost: int) -> (str, int):
    """
    Create link for pay Юкасса
    :return: link for pay and id order
    """

    yoocasa_config: YookassaConfig = await YookassaConfig.objects.afirst()
    Configuration.account_id = yoocasa_config.shop_id
    Configuration.secret_key = yoocasa_config.secret_key_yookassa

    idempotence_key = str(uuid.uuid4())
    user: TgUser = await TgUser.objects.filter(telegram_id=user_id).afirst()
    payment = Payment.create({
        "amount": {
            "value": f"{cost}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"{yoocasa_config.bot_url}"
        },
        "capture": True,
        "description": "Платеж по отчету",
        "save_payment_method": False,
        "metadata": {
            "telegram_id": f"{user_id}",
            'one_time': True,
        }
    },

        idempotence_key
    )

    url = payment.confirmation.confirmation_url

    return url, payment.id