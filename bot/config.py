from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", 25833520))
    API_HASH = getenv("API_HASH", "7d012a6cbfabc2d0436d7a09d8362af7")
    BOT_TOKEN = getenv("BOT_TOKEN", "6450636424:AAEesr6KqJ1b4vIuhauJ21LNEElNecAZqRk")
    PORT = int(getenv("PORT", "8080"))
    BASE_URL = getenv("BASE_URL").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")
    AUTH_CHANNEL = [channel.strip()
                    for channel in getenv("AUTH_CHANNEL").split(",")]
    THEME = getenv("THEME", "quartz")
    USERNAME = getenv("USERNAME", "silent")
    PASSWORD = getenv("PASSWORD", "silent")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "teamsilent")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "admins")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
