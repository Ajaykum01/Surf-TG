from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "29176035"))
    API_HASH = getenv("API_HASH", "35516221c9dd80801bcc2288adcc5d26")
    BOT_TOKEN = getenv("BOT_TOKEN", "7158225681:AAF3Zb_4JpoGa7rbdqBGtUy5apVDI_EM6Gs")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "BQG9MOMAe1oL-MAttLUFptQAfIttlDhKmIvsDQIy9tcxE03DO2wtWJlg2v3oGoshVOLUyLC3RE68OcyXKKYB-Kf5qmJinATpgvNmjuLYFNpuh82LWZwxmRTSPdX8gTVZDMRGk4kJPpS0nqAZLD16xNfhBIKOBllckqqXEKgMU8I4XT1EbF8uObP76UvjuRQPEqegu0W2mqphhwYiazPQYK7yRuCUvIu-FzYPAygX4jGTy0Bwq6Bhf5-8a7p3slzpu84C9YpgZ3z05Kn0bF7lD0Zh2Eyzev1wllmdm_0uLTr12Tb6Y5NFo4KmeIFemYR4-FyVjNvKSRPXheZqfjqYcv12A-OQAAAAB-MK0OAA")
    BASE_URL = getenv("BASE_URL").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL").split(",")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "leo")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "leo")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
