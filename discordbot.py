from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


async def on_ready():
print ("Ready")


@bot.command()
async def (ctx):
author = ctx.message.author
channel = author.voice_channel
    await bot.join_voice_channel(channel)

bot.run(token)
