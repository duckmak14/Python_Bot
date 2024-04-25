import discord
import pytz
from datetime import datetime
from discord.ext import commands

bot = commands.Bot(command_prefix='.', self_bot=True)
BOTTOKEN = ''


@bot.event
async def on_message(message): # Sự kiện khi gửi message
    messageTime = message.created_at # Thời gian gửi messages 
    current_time_utc = datetime.now(pytz.UTC)
    time_difference = current_time_utc - messageTime # Thời gian tính từ lúc gửi đến lúc crawl về
    print(time_difference)
    print(message.guild) # tên của server
    print(message.channel) # tên của channel
    print(message.content) # text messages 
    if message.attachments:
        for attachment in message.attachments:
            print(attachment.url)
    await bot.process_commands(message)

bot.run(BOTTOKEN)