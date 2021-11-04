import asyncio

from buzzword import dp


async def print_webhook_info():
    res = await dp.bot.get_webhook_info()
    print(res)
    return res


def main():
    asyncio.run(print_webhook_info())


if __name__ == "__main__":
    main()
