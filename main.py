import os
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
    major, minor, micro, releaselevel, serial = discord.version_info
    ver = str(major) + '.' + str(minor)

    msg = discord.Embed(description='Meine Informationen', colour=discord.Colour.green(), title='Bot Informationen')
    msg.set_author(name='lala')
    msg.add_field(name='Discord Python Module Version', value=ver, inline=True)
    msg.add_field(name='Blabla', value='1233', inline=True)
    msg.add_field(name='Author', value=msg.author.name, inline=True)

    await ctx.send(embed=msg)


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')


if __name__ == '__main__':

    # At least run execute bot
    bot.run(os.getenv('TOKEN'))
