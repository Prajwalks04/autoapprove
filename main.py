from flask import Flask, request
import os
import logging
from pyrogram import Client

# Load environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Initialize Flask
app = Flask(__name__)

# Initialize Pyrogram bot
bot = Client("auto_approve_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.route("/")
def home():
    return "✅ Bot is alive and healthy on Koyeb!", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_data().decode("utf-8")
    try:
        bot.process_update(bot.parse_update(update))
    except Exception as e:
        logging.error(f"Update processing failed: {e}")
    return "", 200

if __name__ == "__main__":
    import asyncio

    async def start():
        await bot.start()
        await bot.set_webhook(WEBHOOK_URL)
        logging.info("🚀 Bot started and webhook set!")

    asyncio.get_event_loop().run_until_complete(start())

    logging.info("🌐 Flask server starting on port 8080...")
    app.run(host="0.0.0.0", port=8080)
