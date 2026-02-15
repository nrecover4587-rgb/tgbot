# tg_bot/config.py

import os

class Development:
    # Telegram API credentials
    API_ID = int(os.environ.get("API_ID", "24168862"))
    API_HASH = os.environ.get("API_HASH", "916a9424dd1e58ab7955001ccc0172b3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8550727687:AAHZKH_e1eQYdg6RZIbs7VKjGegfgHk18gI")

    # Optional: PostgreSQL URL for database
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://user:pass@host:port/dbname")

    # Optional: Other config variables
    OWNER_ID = int(os.environ.get("OWNER_ID", "8364016757"))
    LOG_GROUP = int(os.environ.get("LOG_GROUP", "-1003556185955"))  # Telegram group for logs
