from os import getenv

DEBUG = bool(getenv("DEBUG", False))

BOT_TOKEN = getenv("TG_BOT_TOKEN")  # get from BotFather

WEBHOOK_HOST = getenv("WEBHOOK_PATH")  # "https://your.domain"
WEBHOOK_PATH = getenv("WEBHOOK_PATH")  # "/path/to/api"

WEBAPP_HOST = getenv("WEBAPP_HOST", "0.0.0.0")  # localhost or ip
WEBAPP_PORT = getenv("WEBAPP_PORT", getenv("PORT", "3000"))  # app port

WEBHOOK_URL = getenv("WEBHOOK_URL", f"{WEBHOOK_HOST}{WEBHOOK_PATH}")


LOGGING_FORMAT = "%(asctime)s %(levelname)-8s [%(name)-16s] (%(filename)s:%(funcName)s:%(lineno)d) %(message)s"  # noqa: E501
