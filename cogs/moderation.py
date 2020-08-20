import discord
from discord.ext import commands
import csv

client = commands.Bot(command_prefix='Bot')

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Online!')

    @client.event
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send('Please ensure you are permitted to use this command!')

    @client.command()
    @commands.has_permissions(manage_guild=True)
    async def change_status(self, ctx, change):
        await client.change_presence(activity=discord.Game(change))

    @change_status.error
    async def status_error(self, ctx, error):
        await ctx.send('Please specify the message!')

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="User Kicked!", description="**{0}** was kicked by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
    
    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title="User Banned!", description="**{0}** was banned by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)

    @client.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="User Unbanned!", description="**{0}** was unbanned by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
                await ctx.send(embed=embed)

    @client.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.add_roles(role)
        embed = discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)

    @client.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.remove_roles(role)
        embed = discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)

    @kick.error
    @ban.error
    @unban.error
    @mute.error
    @unmute.error
    async def userSelect_error(self, ctx, error):
        await ctx.send('Please specify a user!')

    @client.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, amount):
        await ctx.channel.edit(slowmode_delay=int(amount))
        embed = discord.Embed(title="Channel Slowed!", description="**{0}** was slowed by **{1}** !".format(ctx, ctx.message.author, color=0xff00f6))
        await ctx.send(embed=embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        await ctx.send('Please specify an amount for the slowmode!')

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=int):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.send('Please specify an amount of messages to delete!')

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member):
        with open('D:\\Windows Folders\\Documents\\Programming and Scripting\\GitHub\\DiscordBot\\warnings.csv') as file:
            allWarnings = {}
            warnedUser = 0
            reader = csv.DictReader(file)
            for row in reader:
                warnedUser = row[0]
                warning = row[1]
                allWarnings[warnedUser] = warning
            if str(member.id) in allWarnings:
                allWarnings[warnedUser] = str(int(allWarnings[warnedUser]) + 1)
            else:
                allWarnings[warnedUser] = 1
        # channel = client.get_channel(id745980487507640342)
        # Embed = discord.Embed(title="User Warned!", description="**{0}** was warned by **{1}** ! They now have **{2}** warnings!".format(member, ctx.message.author, allWarnings[warnedUser], color=0xff00f6))
        await channel.send("Hello")
        # await client.send.send(discord.Object(id='745980487507640342'), 'hello')


def setup(client):
    client.add_cog(Moderation(client))
