import discord
from discord.ext import commands
import os
import importlib

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def setup_hook():
    # Load /say command if it exists
    if os.path.exists("say/say.py"):
        module = importlib.import_module("say.say")
        await module.setup(bot)

    # GLOBAL sync (can take up to 1 hour to appear)
    await bot.tree.sync()
    print("✅ Global slash commands synced")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN not set")

bot.run(TOKEN)
