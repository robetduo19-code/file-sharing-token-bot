from aiogram import Bot
from app.config import config

async def check_force_sub(bot: Bot, user_id: int):
    if config.FORCE_SUB_CHANNEL == 0:
        return True
    try:
        m = await bot.get_chat_member(config.FORCE_SUB_CHANNEL, user_id)
        return m.status in ("member", "administrator", "creator")
    except:
        return False
