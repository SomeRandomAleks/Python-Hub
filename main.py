import discord
from discord.ext import commands
import asyncio
import json
import typing
import keep_alive
import time
import datetime
import threading
from cogs.defs import *

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")



@client.event
async def on_ready():
	print("Bot is ready")
	guild = client.get_guild(796139098086703145)
	beginner = discord.utils.get(guild.emojis, name="Beginner")
	intermediate = discord.utils.get(guild.emojis, name="Intermediate")
	experienced = discord.utils.get(guild.emojis, name="Experienced")
	await client.change_presence(activity=discord.Game("!help for all commands"))
	embed = discord.Embed(title="Server", description=f"""h""", color=0xffee00)
	
	while True:
	    await asyncio.sleep(17)
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
        if counter >= 8:
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


@client.listen('on_message')
async def help_rotate(message):
    if message.channel.category.id == 807121103993569321:
        await message.channel.edit(
            category=await get_category(message.guild, "Help: Occupied"),
            sync_permissions=True
        )
        await asyncio.sleep(86400)
        await message.channel.edit(
            category=await get_category(message.guild, "Help: Available"),
            sync_permissions=True
        )



client.load_extension('cogs.rr')
client.load_extension('cogs.bump')

@client.listen('on_message')
async def user_bump(message):
    if message.channel.id == 797342261507391488:
        return
    elif message.content == "!d bump":
        await message.delete()
    



            

                
            
    






@client.event
async def on_member_join(member):

	guild_id = member.guild
	channel = client.get_channel(804882935227744266)
	await channel.edit(name=f"Member Count: {guild_id.member_count}")




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

@client.command()
@commands.has_role("Moderation")
async def unmute(ctx, member : discord.Member):

	role = discord.utils.get(ctx.guild.roles, name="Muted")

	if role in member.roles:
		await member.remove_roles(role)
		embed = discord.Embed(title=f"{member} was successfully unmuted", description=f"{ctx.author.mention} unmuted {member}", color=0x1f4454)
		embed.set_thumbnail(url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	else:
		await ctx.send(f"{member} is not already muted")



@client.command()
@commands.has_any_role("Moderation")
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

	guild = client.get_guild(ctx.author.guild.id)
	embed = discord.Embed(title=f"{member} was kicked", description=f"{ctx.author.mention} has kicked {member}\nReason: {reason}", color=0x1f4454)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_footer(text=f"We are now at {guild.member_count} members")

	await ctx.send(embed=embed)


@client.command()
@commands.has_any_role("Moderation")
async def mutev(ctx, member: discord.Member=None, sec=1800):
	if member == None:
		await ctx.send(f"{ctx.author.mention}, you need to specify a member\n```e mutev <@member> <seconds>```")
		return
	else:
		await member.edit(mute=True)
		embed = discord.Embed(title=f"{ctx.author} server muted {member}", description=f"{member} has successfully been server muted\nThey can't talk in VC for {sec} seconds", color=0x1f4454)
		embed.set_thumbnail(url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
		await asyncio.sleep(int(sec))
		await member.edit(mute=False)
		em = discord.Embed(title=f"{member} has been unmuted", description=f"{member} can now talk in voice channels", color=0x1f4454)
		em.set_thumbnail(url=ctx.author.avatar_url)
		await ctx.send(embed=em)



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title='Member Banned', description=f'{member} has been banned by {ctx.author}', color=0x1f4454)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, user=None):

    try:
        user = await commands.converter.UserConverter().convert(ctx, user)
    except:
        await ctx.send("Error: user could not be found!")
        return

    try:
        bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
        if user in bans:
            await ctx.guild.unban(user, reason="Responsible moderator: "+ str(ctx.author))
        else:
            await ctx.send("User not banned!")
            return

    except discord.Forbidden:
        await ctx.send("I do not have permission to unban!")
        return

    except:
        await ctx.send("Unbanning failed!")
        return

    embed = discord.Embed(title="Unban", description=f"{user} was successfully unbanned by {ctx.author}", color=0x1f4454)
    embed.set_thumbnail(url=ctx.author.avatar_url)

    await ctx.send(embed=embed)



@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="")










client.run('Nzk2MTk1OTk1Mjg0NDA2Mjky.X_UZTQ.i0VnCVGWq6wAAGQibtDrNlQowlI')
