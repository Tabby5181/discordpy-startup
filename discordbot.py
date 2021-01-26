import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

bot = commands.Bot(command_prefix="/")
client = discord.Client()
TOKEN = 'ODAzNzAwOTI5Mjk4OTU2Mjg4.YBBm0Q.VVNNVTnfZGNRrytlbpW0v3QNdVc'

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@bot.command(pass_context=True)
async def join(ctx):
author = ctx.message.author
channel = author.voice_channel
await bot.join_voice_channel(channel)

bot.run("token")
