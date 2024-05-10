import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))



SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())




PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**Hᴇʏ ᴛʜᴇʀᴇ! I'ᴍ ᴀ ʀᴇᴀʟʟʏ sᴍᴀʀᴛ ᴀɴᴅ ғᴀsᴛ ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ ᴡɪᴛʜ ᴛᴏᴘ-ɴᴏᴛᴄʜ sᴇᴄᴜʀɪᴛʏ.\n I ᴡᴏɴ'ᴛ ʟᴇᴛ ʏᴏᴜ ᴍᴇssᴀɢᴇ ᴍʏ ᴏᴡɴᴇʀ ᴅɪʀᴇᴄᴛʟʏ ᴜɴʟᴇss ᴛʜᴇʏ sᴀʏ ɪᴛ's ᴏᴋᴀʏ. Rɪɢʜᴛ ɴᴏᴡ, ᴍʏ ᴏᴡɴᴇʀ ɪsɴ'ᴛ ᴏɴʟɪɴᴇ, sᴏ ʏᴏᴜ'ʟʟ ʜᴀᴠᴇ ᴛᴏ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴛʜᴇʏ ɢɪᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ. Aɴᴅ ᴘʟᴇᴀsᴇ, ᴅᴏɴ'ᴛ sᴘᴀᴍ ʜᴇʀᴇ – ɪғ ʏᴏᴜ ᴅᴏ,\n\n I ᴍɪɢʜᴛ ʜᴀᴠᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ғʀᴏᴍ ᴄᴏɴᴛᴀᴄᴛɪɴɢ ᴍʏ ᴏᴡɴᴇʀ.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/cdc9ae0f1a3a7eacf6304.jpg")



LOGGER = logging.getLogger("MADMAX")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

