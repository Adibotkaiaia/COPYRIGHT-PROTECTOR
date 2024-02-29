import os
import logging
import time
import platform
import psutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from config import OWNER_ID, BOT_USERNAME
from config import *
from PROTECTOR import PROTECTOR as app
import pyrogram
from pyrogram.errors import FloodWait

start_txt = """<b> 🤖 ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛᴏʀ 🛡️ </b>

ʜᴇʏ ᴛʜɪs ɪs ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛᴏʀ ʀᴏʙᴏᴛ🤖!\n ᴡᴇ ᴇɴsᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴄᴜʀɪᴛʏ💻 !\n ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ʟᴏɴɢ ᴛᴇxᴛ ᴇᴅɪᴛᴇᴅ ᴍsɢs , ᴀɴᴅ ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴀᴛᴇʀɪᴀʟ...!\nᴊᴜsᴛ ᴀᴅᴅ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ !!\nғᴇᴇʟ ғʀᴇᴇ ғʀᴏᴍ ᴀɴʏ ᴛʏᴘᴇ ᴏғ ᴄᴏᴘʏʀɪɢʜᴛ... ! 🛡! 🤝🔐 """

# Start command handler
@app.on_message(filters.command("rajnishayushilovemaineteranaamdilrkhdiya"))
async def start(_, msg):
    buttons = [
        [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="vip_back")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/3c98dbb4e941e05912697.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

gd_buttons = [
    [
        InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/CHATTING_2024"),
    ]
]

# Back button handler
@app.on_callback_query(filters.regex("vip_back"))
async def vip_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt, reply_markup=InlineKeyboardMarkup(gd_buttons))

#--------------------------------------------------

start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"

# Command to get system information
@app.on_message(filters.command("jarvisxd85"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴊᴀʀᴠɪs ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)

# Forbidden keywords list
FORBIDDEN_KEYWORDS = ["porn", "xxx", "NCERT", "ncert", "ans", "Pre-Medical", " Pollen germination and pollen tube growth are regulated by chemical components of pollen interacting with those of the pistil", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt", "JEE", "ALLEN", "NEET", "jee", "neet", "ans"]

# Message handler to check and delete messages containing forbidden keywords
@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.message_id}")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} Your message contains forbidden keywords.")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.message_id}")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} Your message caption contains forbidden keywords.")
    else:
        await delete_long_edited_messages(_, message)  # Delete long edited messages
        await delete_documents(client, message)  # Check and delete documents

# Define function to check and delete documents
async def delete_documents(client, message):
    if message.document:
        logging.info(f"Deleting document with ID {message.message_id}")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} Please do not send documents in this chat.")

# Delete long edited messages but keep short messages and emoji reactions
async def delete_long_edited_messages(_, edited_message: Message):
    if edited_message.text:
        if len(edited_message.text.split()) > 20:
            await edited_message.delete()
    else:
        if edited_message.sticker or edited_message.animation or edited_message.emoji:
            return

@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    await delete_long_edited_messages(_, edited_message)

# Define a function to filter long messages
def delete_long_messages(_, m):
    return len(m.text.split()) > 20

# Update message handler to delete long messages
@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
