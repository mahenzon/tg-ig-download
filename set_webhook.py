import asyncio
import logging

import config
from buzzword import dp

log = logging.getLogger(__name__)


async def set_webhook():
    log.warning("Set webhook to %r", config.WEBHOOK_URL)
    res = await dp.bot.set_webhook(config.WEBHOOK_URL)
    log.warning("result set webhook %s", res)


def main():
    asyncio.run(set_webhook())


if __name__ == "__main__":
    main()
