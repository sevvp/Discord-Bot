import discord
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands
import os
import asyncio
import random


bot_prefix=("!")
TOKEN = os.getenv("bot_token")

Client = discord.Client()
client = Bot(command_prefix=bot_prefix)

@client.event
async def on_message(message):
  if message.content.startswith('!georgepic'):
    fp = random.choice(os.listdir("folder"))
    await client.send_file(message.channel, "folder/{}".format(fp))

keep_alive()
client.run(TOKEN)