import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler_di import ContextSchedulerDecorator
from django.core.management import BaseCommand

from django.conf import settings
from bot.commands import set_commands

from bot.heandlers.start import start_router
from bot.middleware.apched_middleware import SchedulerMiddleware
from bot.middleware.blocking import UserMiddleware
from bot.misc.logging import configure_logger
from bot.misc.mailing import start_milling


async def on_startup(bot: Bot):
    await set_commands(bot)
    configure_logger(True)


async def main():
    logger = logging.getLogger('Tg')


    logger.info("Starting bot")



    bot = Bot(settings.TG_TOKEN_BOT)

    storage = RedisStorage.from_url(settings.REDIS_URL)

    dp = Dispatcher(storage=storage)

    jobstores = {
        'default': RedisJobStore(

            host=settings.REDIS_HOST,

            port=settings.REDIS_PORT
        )
    }

    scheduler = ContextSchedulerDecorator(
        AsyncIOScheduler(
            timezone="Europe/Moscow",
            jobstores=jobstores
        )
    )

    scheduler.ctx.add_instance(bot, declared_class=Bot)

    scheduler.add_job(
        start_milling,
        'interval',
        # minutes=1,
        seconds=5,
        replace_existing=True,
        id='mailing'
    )

    scheduler.start()

    scheduler.print_jobs()

    dp.message.outer_middleware(UserMiddleware())
    dp.callback_query.outer_middleware(UserMiddleware())
    dp.update.middleware(SchedulerMiddleware(scheduler))

    dp.include_routers(start_router)

    try:
        await on_startup(bot)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except TelegramNetworkError:
        logging.critical('Нет интернета')


class Command(BaseCommand):

    def handle(self, *args, **options):
        asyncio.run(main())
