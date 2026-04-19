import discord
from discord.ext import commands
import os

# هدا الكود بسيط جداً عشان نتأكد إن البوت يشتغل
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ البوت شغال باسم: {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong!')

# حط التوكن بتاعك هنا بين القوسين
token = "حط_التوكن_بتاعك_هنا"
bot.run(token)
