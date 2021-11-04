import asyncio

import config
from buzzword import dp


async def set_webhook():
    await dp.bot.set_webhook(config.WEBHOOK_URL)


def main():
    asyncio.run(set_webhook())


if __name__ == "__main__":
    main()
