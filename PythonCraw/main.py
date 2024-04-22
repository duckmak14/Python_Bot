import discord
import pytz
from datetime import datetime
from discord.ext import commands


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=".",intents=intents)
BOTTOKEN = '' # token của bot được tạo

@bot.event
async def on_message(message): # Sự kiện khi gửi message
    messageTime = message.created_at # Thời gian gửi messages 
    current_time_utc = datetime.now(pytz.UTC)
    time_difference = current_time_utc - messageTime # Thời gian tính từ lúc gửi đến lúc crawl về
    #print(time_difference)
    print(message.guild) # tên của server
    print(message.channel) # tên của channel
    print(message.content) # text messages 
    if message.attachments:
        for attachment in message.attachments:
            print(attachment.url)
    # print(message.attachments[0].url)
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    print("command")
    await ctx.send("hello, I am a discrod bot")
    
bot.run(BOTTOKEN)