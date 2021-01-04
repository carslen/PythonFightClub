import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# load .env file
#
load_dotenv()

client = discord.Client()
bot = commands.Bot(command_prefix='$')

# React on events
#


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

client.run(os.getenv('TOKEN'))

if __name__ == '__main__':

    # At least run execute bot
    client.login(os.getenv('TOKEN'))
    # bot.run(os.getenv('TOKEN'))
