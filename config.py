import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 29791926
API_HASH = "550ae225aaa88c599cf71983f40c86ac"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7925767932:AAGjnDsX3VD1RHc2FUvv0dWeuWB2SY8xz8A"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://HKMUSIC:<db_HKMUSIC@cluster0.vo9ib.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0mongodb+srv://HKMUSIC:<db_HKMUSIC@cluster0.vo9ib.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002342917994

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6720017767

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/hkmusic4"
SUPPORT_GROUP = "https://t.me/hkmusic4"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQHGlrYAasZng6kBWMn4bs80y1JvsDBXMPDgFE4lYBcHyKPLDW_nuurf0GcCWZMjB-E3JnxjE96yjCAWd4JMlUu3Kwc3hmnRfIC3kPmfLJf34ZLXtu0WqK8NuirpW1aJz-sH0q13xe0TiepcfSZS1mbgXgcDb77KYItPtexHvd4JeV-s2w4s6MA35nJeN8ow9KBxQ1uXhYGJF8TxcdGs35iCR2gAUznNoa9HgXsZ3_I1nq-yWm6H2GFUVo9XtP518SaV2gLi-MjgtDSyFbCqQ8Q1bYLNnZ_xqRikJqBlsnD07hh-kGqr7Yue-af-EGunznA7O7MzxMSMj2OyxiKOsL2yFmvyjgAAAAHYaZ78AQBQHGlrYAasZng6kBWMn4bs80y1JvsDBXMPDgFE4lYBcHyKPLDW_nuurf0GcCWZMjB-E3JnxjE96yjCAWd4JMlUu3Kwc3hmnRfIC3kPmfLJf34ZLXtu0WqK8NuirpW1aJz-sH0q13xe0TiepcfSZS1mbgXgcDb77KYItPtexHvd4JeV-s2w4s6MA35nJeN8ow9KBxQ1uXhYGJF8TxcdGs35iCR2gAUznNoa9HgXsZ3_I1nq-yWm6H2GFUVo9XtP518SaV2gLi-MjgtDSyFbCqQ8Q1bYLNnZ_xqRikJqBlsnD07hh-kGqr7Yue-af-EGunznA7O7MzxMSMj2OyxiKOsL2yFmvyjgAAAAHYaZ78AQ"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"

PING_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
STATS_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
STREAM_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpghttps://graph.org/file/b9318f5a48122672b2192-27f14532e0b87f1eef.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
