import os
import asyncio
from fastapi import FastAPI, Request
from pyrogram import Client, filters
from pyrogram.types import Update
from motor.motor_asyncio import AsyncIOMotorClient

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URI = os.environ.get("MONGO_URI")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # full URL, e.g. https://yourapp.koyeb.app/webhook

bot = Client(
    "pyrogram_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# MongoDB
mongo = AsyncIOMotorClient(MONGO_URI)
db = mongo.botdb

# FastAPI app
app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data)
    await bot.dispatcher.feed_update(bot, update)
    return {"ok": True}

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    user = {"id": message.from_user.id, "name": message.from_user.first_name}
    await db.users.update_one({"id": user["id"]}, {"$set": user}, upsert=True)
    await message.reply_text(
        "👋 Welcome to the bot!\n\n✅ You're now registered in the MongoDB database."
    )

@app.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("ℹ️ Available commands:\n/start - Register\n/help - Help")

async def start_bot():
    await bot.start()
    print("Bot started.")
    # Don't call set_webhook — just run webhook server

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
