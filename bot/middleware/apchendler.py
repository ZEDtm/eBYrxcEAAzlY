from admin_panel.models import TgUser
from bot.create_pay import create_repeat_pay
from bot.service_async import get_all_subscribe


async def check_subscribe():
    subscribes = await get_all_subscribe()

    if subscribes:
        for subscribe in subscribes:
            subscribe: TgUser
            subscribe.subscribe = False
            await subscribe.asave()

async def recurment_pay(telegram_id: int) -> None:
    await create_repeat_pay(telegram_id)