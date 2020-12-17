import discord
from discord.ext import commands
import os

prefix = '!'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")

@bot.event
async def on_message(message):
    if message.author.bot:
        return 0
    channel_id = message.channel.id
    send_guild = message.guild
    arg = message.content.split()
    ac = len(arg)
    
    executeLoc = 0
    with open("channel.txt", 'r', encoding='utf-8') as f:
        executeLoc = int(f.read())
    
    if channel_id == executeLoc:
        if arg[0] == "play":
            if ac > 1:
                if arg[1] == "start":
                    if isRun():
                        await message.channel.send(":x: ... 이미 켜져 있는거 같은데요..?\n> 서버를 종료하려면 서버 안에서 `/stop`을 입력해 주세요.")
                    else:
                        await message.channel.send(":white_check_mark: 조금만 기다려 주세요!!")
                        os.chdir("BUKKIT_FILE_LOCATION")
                        os.system("start /wait cmd /c java -jar BUKKIT_FILE_NAME nogui")

token = ''
with open("token.txt", 'r', encoding='utf-8') as f:
    token = f.read()
bot.run(token)
