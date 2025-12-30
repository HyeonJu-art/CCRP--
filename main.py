import discord
from discord.ext import commands
import os
import importlib

# YOUR DEV SERVER ID
DEV_GUILD_ID = 1455415684870701123

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def setup_hook():
    guild = discord.Object(id=DEV_GUILD_ID)

    # Load /say command
    if os.path.exists("say/say.py"):
        module = importlib.import_module("say.say")
        await module.setup(bot)

    await bot.tree.sync(guild=guild)
    print("✅ Slash commands synced to dev server")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN not set")

bot.run(TOKEN)
