# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 29409646))
    API_HASH = os.environ.get("API_HASH", "a69d0340a520c1913c517bea143a3de7)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6132536594:AAGiW566fMpFm3stxkirQKztkCSLQ-5ueLw")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001836119359")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001836119359")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 1))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 25))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "99a34b1b2621e9225d1a")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "oly1VYYD2BCJ10a")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5564974530))

    START_TEXT = """
Hi Unkil, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @AbirHasan2005
"""
    CAPTION = "Video Merged by @{}\n\nMade by @AbirHasan2005"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
