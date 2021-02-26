import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!", intents=intents)



async def get_category(guild, category) -> discord.CategoryChannel:
    return discord.utils.get(guild.categories, name=category)


async def get_text_channel(guild, channel) -> discord.TextChannel:
    return discord.utils.get(guild_id.channels, name=channel)


async def get_voice_channel(guild, channel) -> discord.TextChannel:
    return discord.utils.get(guild_id.channels, name=channel)
    
