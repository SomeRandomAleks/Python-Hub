import discord
from discord.ext import commands
import asyncio
import json
import typing
import keep_alive
import time
import datetime
import threading

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")



@client.event
async def on_ready():
	print("Bot is ready")
	await client.change_presence(activity=discord.Game("!help for all commands"))
	while True:
	    await asyncio.sleep(20)
	    with open('spam.txt', 'r+') as f:
		    f.truncate(0)




keep_alive.keep_alive()

@client.listen('on_message')
async def spam(message):
    counter = 0
    role = discord.utils.get(message.guild.roles, name="Muted")
    with open('spam.txt', 'r+') as file:
        for lines in file:
            if lines.strip('\n') == str(message.author.id):
                counter+=1
        
        file.write(f"{str(message.author.id)}\n")
        if counter >= 7:
            await message.author.add_roles(role)
            embed = discord.Embed(title=f"{message.author} has been muted", description="Reason: Spam\nThey will be unmuted in 30 seconds", color=0x1f4454)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text=time.ctime())
            user_msgs = await message.channel.history(limit=15).flatten()
            for msg in user_msgs:
                if msg.author.id == message.author.id:
                    await msg.delete()
            await message.channel.send(embed=embed)
            await asyncio.sleep(30)
            await message.author.remove_roles(role)
            em = discord.Embed(title=f"{message.author} has been unmuted", description=f"Reason was: Spam", color=0x1f4454)
            em.set_thumbnail(url=message.author.avatar_url)
            em.set_footer(text=time.ctime())
            await message.channel.send(embed=em)




client.load_extension('cogs.bump')

@client.listen('on_message')
async def user_bump(message):
    if message.content == "!d bump":
        await message.delete()
    



            

                
            
    






@client.event
async def on_member_join(member):

	guild_id = member.guild
	channel = client.get_channel(804882935227744266)
	await channel.edit(name=f"Member Count: {guild_id.member_count}")

	em = discord.Embed(title=f"Welcome {member}", description=f"Please verify yourself in {client.get_channel(803826776970231888).mention} to see the rest of the server", color=0x1f4454)
	em.set_footer(text=f"We now have {guild_id.member_count} members!")
	em.set_thumbnail(url=member.avatar_url)

	await client.get_channel(796139098086703148).send(embed=em)



@client.event
async def on_member_remove(member):
	guild_id = member.guild
	channel = client.get_channel(804882935227744266)
	await channel.edit(name=f"Member Count: {guild_id.member_count}")



@client.listen('on_message')
async def not_verify(message):
    if message.channel.id == 803826776970231888:
        if message.author.id != 796195995284406292:
            await message.delete()
        else:
            return
    else:
        return


@client.command()
async def verify(ctx):
	msg = ctx.message
	if ctx.channel.id == 803826776970231888:
    
		await msg.delete()
		role = discord.utils.get(ctx.guild.roles, name="Members")
		await ctx.author.add_roles(role)
		await ctx.send(f"Granted access for {ctx.author.mention}")
	else:
		await msg.delete()
		fail = await ctx.send(f"{ctx.author.mention}, you cannot use that command here")
		await asyncio.sleep(4)
		await fail.delete()

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 807388629595848704:
        role = discord.utils.get(payload.member.guild.roles, name="Bump")
        await payload.member.add_roles(role)


        

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 807388629595848704:
        guild_id = payload.guild_id
        guild = client.get_guild(guild_id)
        role = discord.utils.get(guild.roles, name="Bump")
        if role is not None:
            member = discord.utils.get(guild.members, id=payload.user_id)
            await member.remove_roles(role)
        else:
            print("There is no role named Bump")
        

        



@client.command()
@commands.has_role("Moderation")
async def say(ctx, *, reason):
	embed = discord.Embed(description=reason, color=0x1f4454)
	embed.set_footer(text=time.ctime())
	await ctx.send(embed=embed)

@client.command()
@commands.has_role("Moderation")
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount)+1)
    msg = await ctx.send(f"{ctx.author.mention} cleared {amount} messages")
    await asyncio.sleep(4)
    await msg.delete()

@client.command()
@commands.has_role("Moderation")
async def mute(ctx, member : discord.Member, *, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    embed = discord.Embed(title=f"{member.name} has been muted", description=f"Reason: {reason}", color=0x1f4454)
    embed.set_thumbnail(url=member.avatar_url)










client.run('')
