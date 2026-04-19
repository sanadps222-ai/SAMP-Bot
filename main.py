import discord
from discord.ext import commands
from samp_rcon import RCONClient

TOKEN = 'MTQ3NDkxNjY1NTY3MzkwNTI1Mw.GC4M7T.KaqTJcVaF_sIv3oLdZxdbG83jtkrY_KuGWd5eU'
RCON_PASS = 'd0gj3m6c'
SERVER_IP = '51.83.189.14'
SERVER_PORT = 7777

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def send_rcon(cmd):
    try:
        with RCONClient(SERVER_IP, SERVER_PORT, RCON_PASS) as client:
            return client.send_command(cmd)
    except Exception as e:
        return f"Error: {e}"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Managing SAMP"))
    print(f'Logged in as: {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def bring(ctx, player_id: int):
    send_rcon(f"gethere {player_id}")
    await ctx.send(f"✅ Player {player_id} has been brought.")

@bot.command()
@commands.has_permissions(administrator=True)
async def jail(ctx, player_id: int, time: int, *, reason="Violation"):
    send_rcon(f"jail {player_id} {time} {reason}")
    await ctx.send(f"🔒 Player {player_id} jailed for {time}m. Reason: {reason}")

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, player_id: int):
    send_rcon(f"ban {player_id}")
    await ctx.send(f"🔨 Player {player_id} has been banned.")

bot.run(TOKEN)
