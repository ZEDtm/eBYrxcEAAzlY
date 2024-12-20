import asyncio
import logging

from aiogram import exceptions, Bot
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InputFile
from asgiref.sync import sync_to_async
from loguru import logger

from admin_panel.models import Mailing
from bot.service_async import get_all_users, get_all_maling, get_users_group


async def start_milling(bot: Bot):
    """Поиск запуск неотправленных (по времени) рассылок"""

    mailings = await get_all_maling()
    users = await get_all_users()



    for mailing in mailings:
        mailing: Mailing
        if await mailing.group.aexists():
            users = await get_users_group(mailing.group.all())
        logger.info(f'Starting mailing №{mailing.pk}')
        for user in users:

            args = [user.telegram_id]
            kwargs = {}
            if mailing.media_type in ['photo', 'video', 'document']:

                kwargs['photo'] = mailing.file_id
                kwargs['caption'] = mailing.text

            else:
                args.append(mailing.text)
            kwargs['parse_mode'] = 'HTML'
            await send_message_mailing(bot, mailing.media_type, args, kwargs)
            await asyncio.sleep(1/25)
        mailing.is_sent = True
        await mailing.asave()


async def send_message_mailing(bot, media, args, kwargs) -> None or int:
    """Универсальная функция для отправки сообщения с вложением"""
    send_methods = {
        'photo': bot.send_photo,
        'video': bot.send_video,
        'document': bot.send_document,
        'no_media': bot.send_message,
    }
    send_method = send_methods.get(media)
    try:
        logger.info(f'{kwargs}')
        message = await send_method(*args, **kwargs)
    except exceptions.TelegramForbiddenError as e:
            logger.warning(e)
    except exceptions.TelegramRetryAfter as e:
        logger.warning(f'Flood limit is exceeded. Sleep {e.retry_after} seconds.')
        await asyncio.sleep(e.retry_after)
        logger.info(f'{kwargs}')
        return await send_message_mailing(bot, media, args, kwargs)
    except (exceptions.TelegramAPIError, exceptions.TelegramBadRequest) as e:
        pass
    else:
        logger.info(f'else {kwargs}')
        if media == 'photo':
            file_id = message.photo[-1].file_id
        elif media == 'video':
            file_id = message.video.file_id
        elif media == 'document':
            file_id = message.document.file_id
        else:
            return None

        return file_id

