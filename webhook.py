import logging

from aiogram import Dispatcher
from aiogram.utils.executor import start_webhook

import config
from buzzword import dp as dispatcher

log = logging.getLogger(__name__)


async def on_startup(dp: Dispatcher):
    log.warning("Starting up..")
    # await dp.bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp: Dispatcher):
    # insert code here to run it before shutdown
    log.warning("Shutting down..")


if __name__ == "__main__":
    start_webhook(
        dispatcher=dispatcher,
        webhook_path=config.WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        # skip_updates=True,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
    )
