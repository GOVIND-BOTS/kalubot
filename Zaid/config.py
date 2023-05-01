##Config
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BQBMIi4baSAc7-aTpos9UZ--RQAJ0qv8M981WFmhRrQ2Dm81sKktGJUM-PLnH1OZon9F0VQ46uD3ORkx_De_ihypQZfCUAzjaRj2Jge-AyCIJt1mB414PsGgXfYmZkT0aAERjKcF-P41OVZYpjL57bdeUfI2cqLlP19sssnDFcBksz-bFfLKYKciUEzelNRChhKUdgbtVLvbXjMrHdyP9CSGo1hxiwEv82P-QQwWdKo__j5MKCsCa8OWUltWUdCpEz5zH24gRG8x58kjdyItnqq6UZ9szHZqQtgt-d2Ez5mZGx7GYsnZV428HVQK3VClWHR1A8XJ4bYAf7eE0nCypo1-AAAAAWbanjEA')
BOT_TOKEN = getenv('BOT_TOKEN', '6105046691:AAGfz5sTkZX20EaNW_U2AQ_FCIVQxePAxIk')
API_ID = int(getenv("API_ID", "13976276"))
API_HASH = getenv('API_HASH', '7f024cbc744a2f44569c3641b5ccecb7')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '540000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5348648456').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001982456793'))
ASS_ID = int(getenv("ASS_ID", "6020570673"))
OWNER_ID = list(map(int, getenv('OWNER_ID', '6008136265').split()))
RESULT_PIC = getenv('RESULT_PIC', "https://te.legra.ph/file/38f105acc8beea6779e10.jpg")
PLAYLIST_PIC = getenv('PLAYLIST_PIC', "https://te.legra.ph/file/30b4c615d3258d3a8201f.jpg")
PING_IMG = getenv('PING_IMG', "https://te.legra.ph/file/30b4c615d3258d3a8201f.jpg")
AUTO_LEAVE_TIME = int(getenv("AUTO_LEAVE_ASSISTANT_TIME", "5400"))
AUTO_LEAVE = getenv('AUTO_LEAVING_ASSISTANT', None)
