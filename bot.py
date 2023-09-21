import os
import random
import asyncio
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load configuration from environment variables
TOKEN = os.getenv('BOT_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')
GUILD_ID = int(os.getenv('BOT_GUILD_ID'))
LOG_CHANNEL = int(os.getenv('BOT_LOG_CHANNEL'))
MOD_ROLE_ID = int(os.getenv('BOT_MOD_ROLE_ID'))

# Create the bot instance
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    logging.info(f'Bot is ready | Servers: {len(bot.guilds)}')
    await bot.change_presence(activity=discord.Game(name=random.choice(['Fucking nukers', 'L nukers', 'Security', 'v.1.0'])))

# Event: Message received
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author.top_role.permissions.administrator:
        if str(message.content).count('<@') > 3:
            await message.channel.send(f" <@{message.author.id}> that's a **lot** of pings", delete_after=5)
        return
    else:
        if str(message.content).count('<@') > 3:
            await message.delete()
            overwrite = message.channel.overwrites_for(message.guild.default_role)
            overwrite.send_messages = False
            await message.channel.set_permissions(message.guild.default_role, overwrite=overwrite)
            await message.channel.send(f' <@{message.author.id}> suspicion of massping attack, channel locked')

    await bot.process_commands(message)

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(TOKEN)
