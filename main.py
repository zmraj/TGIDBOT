# Creator : https://t.me/DeltaBotsOfficial >< https://t.me/DeltaBotsOfficial [@DeltaBotsOfficial]

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
 
Telegram = Client(
    "TG_user_ID_Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Telegram.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.id)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

# COMMANDS

START_TEXT = """🆔🆔 Your Telegram ID 🆔🆔 : `{}`"""

# BUTTONS

START_BUTTON = InlineKeyboardMarkup(
             [[
             InlineKeyboardButton('♻️ FIRST JOIN Updates Channel ♻️', url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")
             ]
             [
                        InlineKeyboardButton('🎬𝗠𝗢𝗩𝗜𝗘𝗦🎬', url='https://t.me/joinchat/vii7DDEvKCZkNDVl'),
                        InlineKeyboardButton('💢𝗧𝗩 𝗦𝗘𝗥𝗜𝗘𝗦💢', url='https://t.me/joinchat/Qea8OllY2QUzMDY1')
                    ],
                    [
                       InlineKeyboardButton(" 𝗠𝗢𝗩𝗜𝗘𝗦 𝗕𝗔𝗖𝗞𝗨𝗣 𝗖𝗛𝗔𝗡𝗡𝗘𝗟𝗦 ", url="https://t.me/joinchat/fWTl8WXeWX5kN2Fl")
                       ],
                       [
                       InlineKeyboardButton("⭐️ 𝐌𝐎𝐕𝐈𝐄𝐒 𝐆𝐑𝐎𝐔𝐏 1⭐️", url="https://t.me/joinchat/RSzvS3qax24wMmNl"),
                       InlineKeyboardButton("⭐️ 𝐌𝐎𝐕𝐈𝐄𝐒 𝐆𝐑𝐎𝐔𝐏 2⭐️", url="https://t.me/joinchat/L_lCa57jPUBhNzU1")
                      ],[
                        InlineKeyboardButton('🙋🙋 𝗜𝗡𝗩𝗜𝗧𝗘 𝗬𝗢𝗨𝗥 𝗙𝗥𝗜𝗘𝗡𝗗𝗦 🙋🙋', url='https://telegram.me/share/url?url=https://t.me/joinchat/vii7DDEvKCZkNDVl')
                    ],
                    ]
        )

Telegram.run()
