from pyrogram import filters
from pyrogram.types import ChatMemberUpdated
from pyrogram.handlers import ChatMemberUpdatedHandler
from database import add_group, add_channel

event_handlers = []

# Auto-track group/channel where bot is added
def chat_update_handler(client, update: ChatMemberUpdated):
    if update.new_chat_member and update.new_chat_member.user.is_self:
        chat = update.chat
        if chat.type in ["supergroup", "group"]:
            add_group(chat.id, chat.title)
            print(f"✅ Bot added to group: {chat.title}")
        elif chat.type == "channel":
            add_channel(chat.id, chat.title)
            print(f"✅ Bot added to channel: {chat.title}")

event_handlers.append(ChatMemberUpdatedHandler(chat_update_handler))
