import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ContentTypes

import config
from filtering import (
    instagram_post_link_shortcode_filter,
    instagram_post_link_shortcode_re,
)

# Configure logging
from pics_loading import load_and_send_post_safe

logging.basicConfig(
    level=logging.INFO,
    format=config.LOGGING_FORMAT,
)

log = logging.getLogger(__name__)


# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

if config.DEBUG:
    dp.setup_middleware(LoggingMiddleware())


@dp.message_handler(
    instagram_post_link_shortcode_filter,
    content_types=ContentTypes.TEXT | ContentTypes.PHOTO | ContentTypes.VIDEO,
    # run_task=True,
)
async def respond_with_downloaded_images(message: types.Message):
    text = message.text or message.caption or ""
    shortcodes: list[str] = instagram_post_link_shortcode_re.findall(text)
    log.info("shortcodes %s from text %r", shortcodes, text)

    results = await asyncio.gather(
        types.ChatActions.upload_photo(),
        *[load_and_send_post_safe(message, shortcode) for shortcode in shortcodes],
    )
    log.warning("Results: %s", results)


@dp.message_handler(commands="ping")
async def ping_pong(message: types.Message):
    log.info("send pong")
    await message.reply("pong!")
