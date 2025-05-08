from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['auto_accept_bot']

users_col = db['users']
groups_col = db['groups']
channels_col = db['channels']


def add_user(user_id):
    if not users_col.find_one({"user_id": user_id}):
        users_col.insert_one({"user_id": user_id})


def add_group(chat_id, title):
    if not groups_col.find_one({"chat_id": chat_id}):
        groups_col.insert_one({"chat_id": chat_id, "title": title})


def add_channel(chat_id, title):
    if not channels_col.find_one({"chat_id": chat_id}):
        channels_col.insert_one({"chat_id": chat_id, "title": title})


def get_all_users():
    return [user['user_id'] for user in users_col.find()]


def get_all_groups():
    return groups_col.find()


def get_all_channels():
    return channels_col.find()
