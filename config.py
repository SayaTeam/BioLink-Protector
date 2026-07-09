import re

API_ID = "30422005" # Your Telegram API ID
API_HASH = "5170ded206641d73215baf40175a6924" # Your Telegram API Hash
BOT_TOKEN = "8672398689:AAGxtmvvlwlaTC7Dk1i0hH0w6KoFeQq1WcQ" # Your Bot Token

# MongoDB connection URI
MONGO_URI = "mongodb+srv://shnwazdevv:dev@dev.vj2pnfz.mongodb.net/?appName=dev"

DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute" # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*' #done change here
)
