import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21017005"))
API_HASH = getenv("API_HASH", "031173130fa724e7ecded16064724d96")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6767441538:AAHSn2liQHCYQtflQmaLIFDd9_7HiHCDdS0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://susantamusic:susantabhan@cluster0.5pwi1py.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002062837226"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "2114237158"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/susantabhandari/susantamusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Music_Worldsx")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+aRjpaSweFwQyMWRl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "0"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "1"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 180000000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1900000000))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "BQHAwfwAo80qIT6QkAFIgTHva22w4Gn4D65wZo2TEFvZh-74Cucs0FZSJZ5Sf48mWRnWjRQUSxatKFJQfITWkwxL2uFp3HbRDw3bxecArEPryeliCuFOyNFroJ92Nf6U0kqWKAZ4mcQu3-zahBr2c1AVYmXWk0BqJoB-bWIC5wUB-Zp6t7rKEqaZXuC7xhHr4uUGVtaGtxTOsdPv3_n2AYzCRCfiX00RPCMGOIMcoR1VL5OiTiivXkvASqQzquG4cJKKCgdnRgZf-lkznmGrgxtprHKBOyfrUomN4URHAqXcxc3yJH1yBy0Jr1AFv7DJ7Ld3PR47VvdW5e37R5iuiyeFCmYtngAAAAGd6YQ2AA")
STRING2 = getenv("STRING_SESSION2", "BQG-PTwAXINnQC_KNYdzDra1MlTGONsIIBLCRqNmTSxoX0P54qKQh7yLuFm93Bi3vhhqAgKQonW_t0b9qKpar4cEww8hsT6O5VL0Amf_WxW497L_0oaWVe4KUi3N05nEcBQtX2aev82HGr2HIeH09awdabqcttzgNuGT_cFJ2bEwL_Guh8W7uWzqa3Scu61Q5SYfzhgyFVC3qjHZuJXp-UnRkCxh81oyQ74BZWT7RQFSxQIZvDzOhEDd-M0tH_kgHLuIntYEoP_nCiTy3MtVnV7hI7k5NomG3uYFs44A0WuNvrgvV3-3g8mI_AibyDamgdD5udsxtH4vozQ6qC0ESJnEc8S3_wAAAAGwuDDTAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/5711947ae9bcf3979c6e6.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/6945c42ba53eadb597cd2.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/45b41eea675441ad5dce0.jpg"
STATS_IMG_URL = "https://graph.org/file/49fe9d3eba7ff28a8f5a2.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/81e2d2b3c6b5fcf9098e9.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f0116390593774c1a3d2b.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/5ba8b05b28004a8686faa.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/8f06e566bb55cf9c94d50.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/73f5cbf3b6c6af7b23b5b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/d11c7b33bffee236dc5bc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/d11c7b33bffee236dc5bc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/d11c7b33bffee236dc5bc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
