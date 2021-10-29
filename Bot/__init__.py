from pyrogram import Client
from pyromod import listen

from Bot.vars import Var

API_ID = Var.API_ID
API_HASH = Var.API_HASH
BOT_TOKEN = Var.BOT_TOKEN
LOG_CHANNEL = Var.LOG_CHANNEL

strbot = Client(
    'botSession',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(
        root='Bot.plugins'
    )
)
