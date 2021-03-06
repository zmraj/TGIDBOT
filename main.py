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

START_TEXT = """šš Your Telegram ID šš :\nšššššš\n\n `{}`\n\n\nIF U WANT TO GET YOUR TELEGRAM ID THEN MUST JOIN THIS CHANNEL\n\n@DeltaBotsOfficial\n"""

# BUTTONS

START_BUTTON = InlineKeyboardMarkup(
             [[
             InlineKeyboardButton('ā»ļøšØ FIRST JOIN Updates Channel šØā»ļø', url=f"https://telegram.me/{Config.UPDATE_CHANNEL}")
             ],
             [
                        InlineKeyboardButton('š¬š š¢š©ššš¦š¬', url='https://t.me/joinchat/vii7DDEvKCZkNDVl'),
                        InlineKeyboardButton('š¢š§š© š¦šš„ššš¦š¢', url='https://t.me/joinchat/Qea8OllY2QUzMDY1')
                    ],
                    [
                       InlineKeyboardButton(" š š¢š©ššš¦ šššššØš£ šššš”š”ššš¦ ", url="https://t.me/joinchat/fWTl8WXeWX5kN2Fl")
                       ],
                       [
                       InlineKeyboardButton("ā­ļø šššššš ššššš 1ā­ļø", url="https://t.me/joinchat/RSzvS3qax24wMmNl"),
                       InlineKeyboardButton("ā­ļø šššššš ššššš 2ā­ļø", url="https://t.me/joinchat/L_lCa57jPUBhNzU1")
                      ],[
                        InlineKeyboardButton('šš šš”š©šš§š š¬š¢šØš„ šš„ššš”šš¦ šš', url='https://telegram.me/share/url?url=https://t.me/joinchat/vii7DDEvKCZkNDVl')
                    ],
                    ]
        )

Telegram.run()
