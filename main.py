from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import commands, events

app = Client(
    "auto_accept_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register Handlers
app.add_handler(commands.command_handlers)
app.add_handler(events.event_handlers)

if __name__ == "__main__":
    print("🚀 Bot is starting...")
    app.run()
