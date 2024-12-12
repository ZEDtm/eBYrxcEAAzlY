from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from loguru import logger

from admin_panel.models import TgUser


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if event.from_user.is_bot is False:
            user = await TgUser.objects.filter(telegram_id=event.from_user.id).afirst()
            if user:
                if user.block:
                    await event.answer(text='Вы заблокированы.', show_alert=True)
                    return
            data['tg_user'] = user
        return await handler(event, data)

