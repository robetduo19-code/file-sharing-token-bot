from app.config import config

def is_admin(user_id: int):
    return user_id == config.OWNER_ID or user_id in config.ADMINS
