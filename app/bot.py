from aiogram import Dispatcher, types
from aiogram.filters import CommandStart, Command
from app.database import SessionLocal
from app.models import User, File
from app.services.token_service import create_token, validate_token
from app.services.access_control import check_force_sub
from app.services.admin_service import is_admin
from app.services.analytics_service import log_access
from app.services.referral_service import handle_referral
from app.config import config

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    db = SessionLocal()
    user = db.query(User).filter_by(telegram_id=message.from_user.id).first()
    if not user:
        db.add(User(telegram_id=message.from_user.id))
        db.commit()
        if len(message.text.split()) > 1:
            handle_referral(message.text.split()[1], message.from_user.id)
    db.close()

    args = message.text.split()
    if len(args) > 1:
        if not await check_force_sub(message.bot, message.from_user.id):
            await message.answer("Join the channel first.")
            return
        token = args[1]
        file_id = validate_token(token)
        if not file_id:
            await message.answer("Invalid or expired link.")
            return
        log_access(token, message.from_user.id)
        await message.bot.send_document(message.chat.id, file_id)
    else:
        await message.answer("Welcome to File Sharing Bot")

@dp.message(Command("genlink"))
async def genlink(message: types.Message):
    if not is_admin(message.from_user.id):
        return
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.answer("Reply to a document.")
        return
    db = SessionLocal()
    f = File(tg_file_id=message.reply_to_message.document.file_id)
    db.add(f)
    db.commit()
    token = create_token(f.id, config.VERIFY_EXPIRE)
    db.close()
    bot = await message.bot.get_me()
    await message.answer(f"https://t.me/{bot.username}?start={token}")
