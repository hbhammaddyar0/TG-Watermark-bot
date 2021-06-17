# (c) @hbhammaddyar

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("1853610435:AAGrrCzsK8Whcr4EenHM8ktUo8udLPZsk_w")
	API_ID = int(os.environ.get("4203842", 12345))
	API_HASH = os.environ.get("84fd5643640d6b1e2063d6b6ccf21f8b")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("-1001190978362", 12345))
	UPDATES_CHANNEL = os.environ.get("-1001190978362", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("1160089400", 12345))
	CAPTION = "By @hbhammaddyar"
	BOT_USERNAME = os.environ.get("HBWatermark_bot")
	DATABASE_URL = os.environ.get("mongodb+srv://hbhammaddyar:hbhammaddyar@cluster0.tvqma.mongodb.net/cluster0?retryWrites=true&w=majority")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/kdramashindi).__

Desgined by @hbhammaddyar
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
