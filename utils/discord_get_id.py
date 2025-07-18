#pylint: disable=missing-docstring
#pylint: disable=import-error
#pylint: disable=line-too-long

# /// script
# requires-python = ">=3.13"
# dependencies = [
#    "discord.py>=2.5.2"
# ]
# ///

import discord
from discord.ext import commands

BOT_TOKEN = ""  # Discord bot token (required for authentication)

intents = discord.Intents.default()
# IMPORTANT: Remember to enable this option in the Discord Developer Portal for your bot; otherwise, commands will not work.
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot: {bot.user.name} up and running!")
    print('------')

@bot.command()
async def id(ctx): #pylint: disable=redefined-builtin
    await ctx.reply(f"This channel ID is: `{str(ctx.channel.id)}`")

bot.run(BOT_TOKEN)
