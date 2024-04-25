from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from Bot import strbot

START_MESSAGE = (
        "Hello Dear User\n"
        "I'm the String Session Generator Bot\n\n"
        "Please tap on the button blow to start the process" 
    )

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='✨ Generate String Session ✨', callback_data='sele_telethon')]]
)

@strbot.on_message(filters.command('generate'))
async def start(strbot, message):
    await message.reply(
        text=START_MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=True
    )
