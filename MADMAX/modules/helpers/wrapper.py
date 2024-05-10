from pyrogram.types import *
from traceback import format_exc

from ...console import SUDOERS
from ..clients.clients import app, bot

def super_user_only(mystic):
    async def wrapper(client, message):
        try:
            if message.from_user.is_self:
                return await mystic(client, message)
        except:
            if message.outgoing:
                return await mystic(client, message)
            
    return wrapper



def sudo_users_only(mystic):
    async def wrapper(client, message):
        try:
            if (message.from_user.is_self or
               message.from_user.id in SUDOERS
            ):
                return await mystic(client, message)
        except:
            if (message.outgoing or
               message.from_user.id in SUDOERS
            ):
                return await mystic(client, message)
            
    return wrapper
    

def cb_wrapper(func):
    async def wrapper(bot, cb):
        sudousers = SUDOERS
        if (cb.from_user.id != app.me.id and
            cb.from_user.id not in sudousers
        ):
            return await cb.answer(
                "❎ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀ sᴜᴅᴏ ᴜsᴇʀ❗",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                return await func(bot, cb)
            except Exception:
                print(format_exc())
                return await cb.answer(
                    f"❎ sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʟᴏɢs❗..."
                )
        
    return wrapper


def inline_wrapper(func):
    from ... import __version__
    async def wrapper(bot, query):
        sudousers = SUDOERS
        if (query.from_user.id != app.me.id and
            query.from_user.id not in sudousers
        ):
            try:
                button = [
                    [
                        InlineKeyboardButton(
                            "【 ᴍᴀᴅᴍᴀx ✘ ᴜsᴇʀʙᴏᴛ 】",
                            url=f"https://github.com/THEMADMAXPRO/MADMAXUSERBOT"
                        )
                    ]
                ]
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultPhoto(
                                photo_url=f"https://telegra.ph/file/6aedd44027c5b84ef5a09.jpg",
                                title="ᴍᴀᴅᴍᴀx ✘ ᴜsᴇʀʙᴏᴛ",
                                thumb_url=f"https://telegra.ph/file/6aedd44027c5b84ef5a09.jpg",
                                description=f"【 ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴍᴀᴅᴍᴀx ✘ ᴜsᴇʀʙᴏᴛ ...】",
                                caption=f"<b>➻ ᴡᴇʟᴄᴏᴍᴇ » ᴛᴏ » ᴍᴀᴅᴍᴀx \n✅ ᴜsᴇʀʙᴏᴛ {__version__} ✨...</b>",
                                reply_markup=InlineKeyboardMarkup(button),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title="",
                                input_message_content=InputTextMessageContent(
                                    f"||**➻ ᴘʟᴇᴀsᴇ, ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴍᴀᴅᴍᴀx ✘ ᴜsᴇʀʙᴏᴛ❗...\n\nʀᴇᴘᴏ:** <i>https://github.com/THEMADMAXPRO/MADMAXUSERBOT/</i>||"
                                ),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                pass
        else:
           return await func(bot, query)

    return wrapper

