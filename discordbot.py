import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

bot = commands.Bot(command_prefix="/")
client = discord.Client()
TOKEN = os.environ['DISCORD_BOT_TOKEN']

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
