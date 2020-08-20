import discord
from discord.ext import commands
from time import ctime
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
        embed = discord.Embed(title="User Muted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)

    @client.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, amount):
        await ctx.channel.edit(slowmode_delay=int(amount))
        embed = discord.Embed(title="Channel Slowed!", description="**{0}** was slowed by **{1}** !".format(ctx, ctx.message.author, color=0xff00f6))
        await ctx.send(embed=embed)

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        amount = amount+1
        await ctx.channel.purge(limit=amount)

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member):
        allWarnings = 0
        with open ("D:\Windows Folders\Documents\Programming and Scripting\GitHub\DiscordBot\warnings.csv", "r") as file:
            filereader = csv.reader(file)
            for row in filereader:
                for field in row:
                    if field == member:
                        allWarnings = int(row[1])
                        username = str(row[0])
                        print(username)
                        print(allWarnings)

        channel = self.client.get_channel(745980487507640342)
        embed = discord.Embed(title="User Warned!", description="**{0}** was warned by **{1}** ! They now have **{2}** warnings!".format(member, ctx.message.author, allWarnings, color=0xff00f6))
        await channel.send(embed=embed)

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def report(self, ctx, member: discord.Member, reason):
        channel = self.client.get_channel(746090781961617462)
        embed = discord.Embed(title="Report Submitted!", description="**{0}** was reported by **{1}** at **{2}** for **{3}**".format(member, ctx.message.author, ctime(), reason, color=0xff00f6))
        await channel.send(embed=embed)

    @client.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member: discord.Member, choice):
        role = discord.utils.get(member.guild.roles, name=choice)
        await member.add_roles(role)

    @client.command()
    @commands.has_permissions(manage_roles=True)
    async def remrole(self, ctx, member: discord.Member, choice):
        role = discord.utils.get(member.guild.roles, name=choice)
        await member.remove_roles(role)


def setup(client):
    client.add_cog(Moderation(client))
