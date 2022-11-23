# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 6425084))
    API_HASH = os.environ.get("API_HASH", "8061114222ed0679410ed400875d754f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5864237669:AAHc1v2QKuOGgbFKJNyQQzbnOwevfsiCkCQ")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001555769566")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 1))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 25))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Cluster0:password17@cluster0.lzclww3.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1213093212))

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
