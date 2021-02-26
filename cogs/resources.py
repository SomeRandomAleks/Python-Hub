import discord
from discord.ext import commands
import datetime

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!", intents=intents)
python_hub = "https://cdn.discordapp.com/attachments/814986274158805033/814986385429758012/Python_Hub_1.png"
guild = client.get_guild(796139098086703145)
datetime_now = datetime.datetime.now()
current_time = datetime_now.strftime("%H:%M")


async def get_category(guild, category) -> discord.CategoryChannel:
    return discord.utils.get(guild.categories, name=category)


async def get_text_channel(guild, channel) -> discord.TextChannel:
    return discord.utils.get(guild_id.channels, name=channel)


async def get_voice_channel(guild, channel) -> discord.TextChannel:
    return discord.utils.get(guild_id.channels, name=channel)
    
