import discord
from discord import app_commands

@app_commands.command(
    name="say",
    description="Make the bot say a message"
)
@app_commands.checks.has_permissions(manage_messages=True)
async def say(
    interaction: discord.Interaction,
    message: str
):
    await interaction.channel.send(message)
    await interaction.response.send_message(
        "✅ Message sent.",
        ephemeral=True
    )

async def setup(bot):
    bot.tree.add_command(say)
