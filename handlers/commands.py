from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from config import OWNER_ID
from database import (
    add_user, get_all_users,
    get_all_groups, get_all_channels
)
from broadcast import broadcast_message

command_handlers = []

# /start command
def start_cmd(client, message: Message):
    add_user(message.from_user.id)
    message.reply_text("👋 Welcome! I'm active and auto-accepting users where allowed.")
command_handlers.append(MessageHandler(start_cmd, filters.command("start")))

# /help command
def help_cmd(client, message: Message):
    message.reply_text(
        "**🤖 Bot Commands:**\n"
        "/start - Register yourself\n"
        "/help - Show this help message\n"
        "/broadcast - Send message to users/groups/channels (admin only)\n"
        "/users - Show total users\n"
        "/groups - List added groups\n"
        "/channels - List added channels"
    )
command_handlers.append(MessageHandler(help_cmd, filters.command("help")))

# /broadcast (admin only)
def broadcast_cmd(client, message: Message):
    if message.from_user.id != OWNER_ID:
        return message.reply("🚫 You are not authorized.")

    if not message.reply_to_message:
        return message.reply("❗️Reply to a message to broadcast.")

    target_msg = message.reply_to_message
    message.reply("📣 Broadcasting...")
    broadcast_message(client, target_msg)
command_handlers.append(MessageHandler(broadcast_cmd, filters.command("broadcast")))

# /users
def users_cmd(client, message: Message):
    if message.from_user.id != OWNER_ID:
        return
    users = get_all_users()
    message.reply_text(f"👥 Total users: {len(users)}")
command_handlers.append(MessageHandler(users_cmd, filters.command("users")))

# /groups
def groups_cmd(client, message: Message):
    if message.from_user.id != OWNER_ID:
        return
    groups = get_all_groups()
    msg = "\n".join([f"{g['title']} (`{g['chat_id']}`)" for g in groups])
    message.reply_text(f"📘 Groups:\n{msg or 'None'}", disable_web_page_preview=True)
command_handlers.append(MessageHandler(groups_cmd, filters.command("groups")))

# /channels
def channels_cmd(client, message: Message):
    if message.from_user.id != OWNER_ID:
        return
    channels = get_all_channels()
    msg = "\n".join([f"{c['title']} (`{c['chat_id']}`)" for c in channels])
    message.reply_text(f"📗 Channels:\n{msg or 'None'}", disable_web_page_preview=True)
command_handlers.append(MessageHandler(channels_cmd, filters.command("channels")))
