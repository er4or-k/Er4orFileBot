#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather

# Telegram Bot Token
TG_BOT_TOKEN = os.environ.get("6575853231:AAGAnr-5Aa4HeWzG92GtAivIW4fnl2c5kOQ")
if not TG_BOT_TOKEN:
    raise ValueError("Environment variable 'TG_BOT_TOKEN' is not set.")

# Your API ID from my.telegram.org
APP_ID = os.environ.get("29788419")
if APP_ID is None:
    raise ValueError("Environment variable 'APP_ID' is not set.")
try:
    APP_ID = int(APP_ID)
except ValueError:
    raise ValueError("Environment variable 'APP_ID' must be a valid integer.")

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("64889bdac00a24eabcb02811da11a4f6")
if not API_HASH:
    raise ValueError("Environment variable 'API_HASH' is not set.")

# Your db channel ID
CHANNEL_ID = os.environ.get("-1001610809402")
if CHANNEL_ID is None:
    raise ValueError("Environment variable 'CHANNEL_ID' is not set.")
try:
    CHANNEL_ID = int(CHANNEL_ID)
except ValueError:
    raise ValueError("Environment variable 'CHANNEL_ID' must be a valid integer.")

# Owner ID
OWNER_ID = os.environ.get("6960629549")
if OWNER_ID is None:
    raise ValueError("Environment variable 'OWNER_ID' is not set.")
try:
    OWNER_ID = int(OWNER_ID)
except ValueError:
    raise ValueError("Environment variable 'OWNER_ID' must be a valid integer.")

# Port (default to 8080)
PORT = os.environ.get("PORT", "8080")
try:
    PORT = int(PORT)
except ValueError:
    raise ValueError("Environment variable 'PORT' must be a valid integer.")

# Database URI
DB_URI = os.environ.get("mongodb+srv://er4orkofficial:L1UZfWek0WzIe64B@cluster0.tuupc.mongodb.net/er4orfiledb?retryWrites=true&w=majority")
if not DB_URI:
    raise ValueError("Environment variable 'DB_URI' is not set.")

# Database Name
DB_NAME = os.environ.get("er4orfiledb")
if not DB_NAME:
    raise ValueError("Environment variable 'DB_NAME' is not set.")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
