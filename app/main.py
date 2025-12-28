from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from aiogram import Bot
from app.bot import dp
from app.config import config
from app.api.admin import router as admin_router

bot = Bot(token=config.TG_BOT_TOKEN)
app = FastAPI()
app.include_router(admin_router)

@app.post("/webhook")
async def webhook(req: Request):
    await dp.feed_raw_update(bot, await req.json())
    return {"ok": True}

@app.get("/admin")
def admin():
    return FileResponse("frontend/index.html")

@app.get("/admin.jsx")
def admin_js():
    return FileResponse("frontend/admin.jsx")
