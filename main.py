import os
import sys
import discord
from dotenv import load_dotenv
from discord.ext import commands

# load .env file
#
load_dotenv()

# Create bot object
#
bot = commands.Bot(command_prefix='$', description='my very first Discord Bot')


# React on events
#
@bot.event
async def on_ready():
    print('Logged in as', bot.user.name, '(with ID {}, {})'.format(bot.user.id, bot.user))
    print('--------------------')
    print('We have logged in as {0.user}'.format(bot))


# define bot commands
#
@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def echo2(ctx, arg):
    await ctx.send(ctx.message)


@bot.command()
async def test(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


@bot.command()
async def test2(ctx):
    # await ctx.send('Discord Python Module Version: {0}.Major.{1}.Minor.{2}'.format(discord.version_info))
    major, minor, micro, releaselevel, serial = discord.version_info
    ver = 'Discord Python Module Version: ' + str(major) + '.' + str(minor)
    await ctx.send(ver)


@bot.command()
async def info(ctx):
    major, minor, micro, releaselevel, serial = sys.version_info
    p_ver = str(major) + '.' + str(minor) + '.' + str(micro)
    msg = discord.Embed(description='Meine Informationen', colour=discord.Colour.green(), title='Bot Informationen')
    msg.add_field(name='Verwendete Software', value='Name und Version der verwendeten Softwarekomponenten.', inline=False)
    msg.add_field(name='discord.py', value=discord.__version__)
    msg.add_field(name='Python', value=p_ver)
    msg.add_field(name='Author', value='cle', inline=False)
    msg.add_field(name='Source Code', value='https://github.com/carslen/PythonFightClub')

    await ctx.send(embed=msg)


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')


if __name__ == '__main__':

    # At least run execute bot
    bot.run(os.getenv('TOKEN'))
