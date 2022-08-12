from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10069388"))
API_HASH = getenv("API_HASH", "87c1643359aed164979679e4c3475c1d")
BOT_TOKEN = getenv("BOT_TOKEN","5396553905:AAGTjeHg3KX77lt0-WZ-m5deoiK0k06K08w")
BOT_NAME = getenv("BOT_NAME","💖ꜛ⟬꯭࿊꯭ɴ꯭፝֟𝐄 ꯭꯭༓ ꯭𝐋꯭ᴏ፝֟ꪜ꯭𝐄 ꯭༓꯭ 𝐌꯭ᴜ꯭፝֟sɪ꯭𝐂꯭⟭ꜛ💖")
BOT_USERNAME = getenv("BOT_USERNAME", "One_love_music_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "king_of_izzy")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "tamil_chat_junctions")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/eb5c8960da2c2f22f8303.jpg")
PING_IMG = getenv("PING_IMG", "")
SESSION_NAME = getenv("SESSION_NAME","BQAw5bva08L_p04tuYinQJiJFScGxhgU0hshrZDbwvpu2fAQ4yJotezjk2O1MMDvDMqy3csGBtNpbU7hEU3WoBXqBVRsO4FVVFhgeEJ4zvGyCYz_jyJ22EMwLiTMiVEXxjytw70OIY9anG9xBysgXmsP4se-5LVGkgq6jBe1U6tZIB2hRnLqnTonu_WkE59kmU9aNIbwrfh6W4jMU43msi-Lv2Ru8LMqVmTIg2MNNkw4G-dtZTeMNb_YSErtmsGgblDTGpmYOVfUqV-eR9Obzr6cMM8q0Tx4eb_98vAWROb3I0THCyv6YmHriOWouDqgK5FQIiokbNT6FbpKHV1X6cIBAAAAAUr0aIEA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5552498817").split()))
