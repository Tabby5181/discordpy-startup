import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

bot = commands.Bot(command_prefix="|")
client = discord.Client()

async def on_ready():
print ("Ready")

@bot.command(pass_context=True)
async def join(ctx):
author = ctx.message.author
channel = author.voice_channel
await bot.join_voice_channel(channel)

bot.run("token")
