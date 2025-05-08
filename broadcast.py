from database import get_all_users, get_all_groups, get_all_channels
from pyrogram.errors import FloodWait
import asyncio

async def try_send(client, chat_id, message):
    try:
        await message.copy(chat_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await try_send(client, chat_id, message)
    except Exception:
        pass  # Ignore failures

def broadcast_message(client, message):
    async def broadcast():
        # Broadcast to users
        for user_id in get_all_users():
            await try_send(client, user_id, message)

        # Broadcast to groups
        for group in get_all_groups():
            await try_send(client, group["chat_id"], message)

        # Broadcast to channels
        for channel in get_all_channels():
            await try_send(client, channel["chat_id"], message)

    client.loop.create_task(broadcast())
