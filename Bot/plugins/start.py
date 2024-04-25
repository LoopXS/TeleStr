from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from Bot import strbot

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='✨ Generate String Session ✨', callback_data='sele_telethon')]]
)

@strbot.on_message(filters.command('session'))
async def start(strbot, message):
    await message.reply(
        text=(f"Hey {message.from_user.mention}, please tap on the button below to start the process"),
        reply_markup=KEYBOARD,
        disable_web_page_preview=True
    )
