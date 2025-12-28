import os

class Config:
    TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL")

    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    ADMINS = list(map(int, os.getenv("ADMINS", "").split()))

    FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", "0"))
    VERIFY_EXPIRE = int(os.getenv("VERIFY_EXPIRE", "86400"))

    ADMIN_KEY = os.getenv("ADMIN_KEY", "CHANGE_ME")

config = Config()
