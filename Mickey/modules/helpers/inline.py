from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Mickey import OWNER
from Mickey import MickeyBot

DEV_OP = [
    [
        InlineKeyboardButton(text="✯ 𝐎ᴡɴᴇʀ ✯", user_id="5710889435"),
        InlineKeyboardButton(text="✯ 𝐒ᴜᴘᴘᴏʀᴛ ✯", url=f"https://t.me/yaaro_ki_mehfil_group"),
    ],
    [
        InlineKeyboardButton(
            text="✯ 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ ✯",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐇ᴇʟᴘ & 𝐂ᴍᴅs ✯", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐒ᴏᴜʀᴄᴇ ✯", url="https://graph.org/file/57ef19d4c10b830cafb0f.jpg"),
        InlineKeyboardButton(text="✯ 𝐀ʙᴏᴜᴛ ✯", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="✯ 𝐀ᴅᴅ 𝐌ᴇ 𝐁ᴀʙʏ ✯",
            url=f"https://t.me/{MickeyBot.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="✯ 𝐂ʟᴏsᴇ ✯",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="✯ 𝐂ʜᴀᴛʙᴏᴛ ✯", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="✯ 𝐓ᴏᴏʟs ✯", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="BACK"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="𝐄ɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="𝐃ɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="✯𝐒ᴏᴏᴍ✯", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="SBACK"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="✯ 𝐇ᴇʟᴘ ✯", callback_data="HELP"),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="✯ 𝐇ᴇʟᴘ ✯", url=f"https://t.me/{MickeyBot.username}?start=help"
        ),
        InlineKeyboardButton(text="✯ 𝐂ʟᴏsᴇ ✯", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="✯ 𝐒ᴜᴘᴘᴏʀᴛ ✯", url=f"https://t.me/yaaro_ki_mehfil_group"),
        InlineKeyboardButton(text="✯ 𝐇ᴇʟᴘ ✯", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐎ᴡɴᴇʀ ✯", user_id="6481280351"),
        InlineKeyboardButton(text="✯ 𝐒ᴏᴜʀᴄᴇ ✯", url="https://t.me/Santani_hu_bro"),
    ],
    [
        InlineKeyboardButton(text="✯ 𝐔ᴘᴅᴀᴛᴇs ✯", url="https://t.me/official_mr_king"),
        InlineKeyboardButton(text="✯ 𝐁ᴀᴄᴋ ✯", callback_data="BACK"),
    ],
]
