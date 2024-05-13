import discord
import requests
import sys
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
from datetime import datetime

# Format is [SUBJECT] [CLASS CODE] [SECTION ROW] [TABLE ROW]
COURSES = [
    ["CS", "241", 1, 3],
    ["CS", "240", 3, 3],
    ["MATH", "239", 5, 3],
    ["MATH", "239", 7, 3],
    ["HEALTH", "105", 1, 2],
]

load_dotenv()

# Discord bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# IDs for notification on the server
notif_channel_id = int(os.getenv('CMOGGER_NOTIF_ID'))
user_id = int(os.getenv('CMOGGER_USER_ID'))

# Discord bot token
TOKEN = os.getenv('CMOGGER_TOKEN')

def read_courses():
    pass

def check(COURSE):
    boxes = []
    url = f"https://classes.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?level=under&sess=1245&subject={COURSE[0]}&cournum={COURSE[1]}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    line = soup.find_all("tr")[COURSE[3]].findChildren("tr")[COURSE[2]]

    for element in line:
        boxes.append(element.text.strip())

    
    if int(boxes[7]) < int(boxes[6]): return True, boxes[1], boxes[0]
    else: return False, boxes[1], boxes[0]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    sys.stdout.flush()
    check_courses.start()

@tasks.loop(seconds=69)
async def check_courses():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{dt_string}]")
    print("Checking...")
    for i in range(len(COURSES)):
        cl, sec, cnum = check(COURSES[i])
        print(f"{COURSES[i][0]}{COURSES[i][1]} {sec} ({cnum})")
        if cl:
            print("Spot Found") 
            channel = bot.get_channel(notif_channel_id)
            await channel.send(f"<@{user_id}> There's an open spot in {COURSES[i][0]}{COURSES[i][1]} {sec} ({cnum})")
    sys.stdout.flush()

@check_courses.before_loop
async def before_check_courses():
    print('Waiting for bot to be ready...')
    user = await bot.fetch_user(user_id)
    await user.send("I am online and ready to mog")
    sys.stdout.flush()

bot.run(TOKEN)
