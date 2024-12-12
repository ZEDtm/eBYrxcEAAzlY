import asyncio
import logging
import sys
from collections import defaultdict
from os import getenv
from datetime import datetime

import aiohttp
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import string, random

# Bot token can be obtained via https://t.me/BotFather
TOKEN = '6819523929:AAHHn_2yAPrP0a7BU8dXouvh7ivDxJUg5O0'

# FastAPI server URL
FASTAPI_URL = "http://localhost:4000/api/newMessage"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

processed_photos = defaultdict(set)
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Пошел нахуй, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message to the FastAPI server
    """

    try:
        # Prepare the message data
        message_data = {
            "user": message.chat.id,
            "message": {
                "id": message.message_id,
                "text": message.text or "",
                "status": "sent",
                "sender": message.chat.id,
                "recipient": 0,
                "date": int(message.date.timestamp()),
                "files": []
            }
        }

        # Add files if any
        if message.photo:
            # Get the photo with the highest resolution
            photo = max(message.photo, key=lambda p: p.width * p.height)
            file_data = {
                "file_name": await generate_random_string(10),
                "file_id": photo.file_id,
                "file_size": photo.file_size,
                "mime_type": "image/jpeg"  # Assuming all photos are JPEG
            }
            message_data["message"]["files"].append(file_data)

        if message.document:
            file_data = {
                "file_name": await generate_random_string(10),
                "file_id": message.document.file_id,
                "file_size": message.document.file_size,
                "mime_type": message.document.mime_type
            }
            message_data["message"]["files"].append(file_data)

        if message.video:
            file_data = {
                "file_name": await generate_random_string(10),
                "file_id": message.video.file_id,
                "file_size": message.video.file_size,
                "mime_type": message.video.mime_type
            }
            message_data["message"]["files"].append(file_data)

        # if message.media_group_id:
        #     # Handle media group (multiple photos, documents, or videos)
        #     if message.photo:
        #         # Get the photo with the highest resolution
        #         photo = max(message.photo, key=lambda p: p.width * p.height)
        #         # Check if the photo has already been processed in this media group
        #         if photo.file_id not in processed_photos[message.media_group_id]:
        #             file_data = {
        #                 "file_name": await generate_random_string(10),
        #                 "file_id": photo.file_id,
        #                 "file_size": photo.file_size,
        #                 "mime_type": "image/jpeg"  # Assuming all photos are JPEG
        #             }
        #             message_data["message"]["files"].append(file_data)
        #             # Mark the photo as processed
        #             processed_photos[message.media_group_id].add(photo.file_id)
        #
        #     if message.document:
        #         for document in message.document:
        #             file_data = {
        #                 "file_name": await generate_random_string(10),
        #                 "file_id": document.file_id,
        #                 "file_size": document.file_size,
        #                 "mime_type": document.mime_type
        #             }
        #             message_data["message"]["files"].append(file_data)
        #
        #     if message.video:
        #         for video in message.video:
        #             file_data = {
        #                 "file_name": await generate_random_string(10),
        #                 "file_id": video.file_id,
        #                 "file_size": video.file_size,
        #                 "mime_type": video.mime_type
        #             }
        #             message_data["message"]["files"].append(file_data)

        # Send the message data to FastAPI server
        print(message_data)
        headers = {
            'Authorization': f'Bearer {TOKEN}'
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(FASTAPI_URL, headers=headers, json=message_data) as response:
                if response.status != 200:
                    logging.error(f"Failed to send message to FastAPI: {await response.text()}")
                else:
                    logging.info("Message sent to FastAPI successfully")

    except Exception as e:
        logging.error(f"Error processing message: {e}")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)

async def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())