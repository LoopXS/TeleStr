from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from Bot import strbot

START_MESSAGE = (f"Hey {mention}\nI'm the String Session Generator Bot\nPlease tap on the button blow to start the process")

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='✨ Generate String Session ✨', callback_data='sele_telethon')]]
)

@strbot.on_message(filters.command('session'))
async def start(strbot, message):
    user = await strbot.get_me()
    mention = user.mention
    await message.reply(
        text=START_MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=True
    )
