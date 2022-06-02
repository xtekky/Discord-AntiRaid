import requests, discord, threading, random, json, asyncio, time, cursor, os
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

# -------------- config ----------------
CONF = {
    "token": "BOT_TOKEN_HERE",
    "prefix": "PREFIX_HERE",
    "name": "BOT_NAME"
    "guild_id": 0,
    "other": {
        "log_channel": "",
        "blacklisted": [           # These configs don't have any use yet but will as I improve the bot
 
        ],
    "mod_role": "",
    "mod_role_id": 0,       
    }


}


# --------------- other ----------------
os.system('cls' if os.name == 'nt' else 'clear')
os.system(f'title {CONF["name"]} v1 ~ Starting...' if os.name == 'nt' else '')
cursor.hide()
start = time.time()

bot = commands.AutoShardedBot(
        command_prefix = CONF["prefix"], 
        help_command = None, 
        intents = discord.Intents().all()
    )

pings = 0


# --------------- main ----------------

@bot.event
async def on_ready():
    print(f' [startup] Ready ({round(time.time()-start, 1)}s) | Servers: {len(bot.guilds)}')
    os.system('title Security v1 ~ Online' if os.name == 'nt' else '')

    while True:
        activity = discord.Activity(type=discord.ActivityType.playing, name=random.choice([f'Fucking nukers', 'L nukers', 'Sercurity', 'v.1.0']))
        await bot.change_presence(activity=activity)
        await asyncio.sleep(10)


@bot.event
async def on_message(ctx):
    try:
        if ctx.author == bot.user:
            return
        
        if ctx.author.top_role.permissions.administrator is True:
            
            if str(ctx.content).count('<@') > 3:
                await ctx.channel.send(f" <@{ctx.author.id}> that's a **lot** of pings", delete_after=5)
            return

        else:
            if str(ctx.content).count('<@') > 3:
                await ctx.delete()
                
                overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = False
                await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                await ctx.channel.send(f' <@{ctx.author.id}> supicion of massping attack, channel locked')
                
    except Exception as e:
        await ctx.channel.send(e)


bot.run(CONF["token"])
