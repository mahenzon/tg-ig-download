import logging
import pathlib

import instaloader
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import config

# Configure logging
logging.basicConfig(level=logging.INFO, format=config.LOGGING_FORMAT)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

if config.DEBUG:
    dp.setup_middleware(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


def main():
    # Get instance
    loader = instaloader.Instaloader()

    # URL = "https://www.instagram.com/p/CVw7-n6MV5A/?utm_medium=copy_link"
    post_shortcode = "CVw7-n6MV5A"

    post = instaloader.Post.from_shortcode(loader.context, post_shortcode)
    target = pathlib.Path("./pic").resolve()
    loader.download_post(post=post, target=target)


if __name__ == "__main__":
    main()
