import discord
from discord.ext import commands
from time import ctime
import sqlite3
import json
client = commands.Bot(command_prefix='!')

with open('config.json') as configFile:
    data = json.load(configFile)
    for value in data["server_details"]:
        warn_id = value['warnings_id']
        report_id = value['reports_id']


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Online!')


    @client.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="User Kicked!", description="**{0}** was kicked by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
    
    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
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
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, amount):
        await ctx.channel.edit(slowmode_delay=int(amount))
        embed = discord.Embed(title="Channel Slowed!", description="**{0}** was slowed by **{1}** !".format(ctx.channel, ctx.message.author, color=0xff00f6))
        await ctx.send(embed=embed)

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        amount = amount+1
        await ctx.channel.purge(limit=amount)

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member):
        allWarnings = 1
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        records = cursor.execute("SELECT username, warnings FROM warnings WHERE username = ?", [str(member)]).fetchall()
        for row in records:
            allWarnings = row[1] + 1
        cursor.execute("SELECT username, warnings FROM warnings WHERE username = ?", [str(member)])
        result = cursor.fetchone()
        if result:
            cursor.execute("UPDATE warnings SET warnings = ? WHERE username = ?", [allWarnings, str(member)])
        else:
            cursor.execute('''INSERT INTO warnings(username, warnings) VALUES(?,?)''', (str(member), allWarnings))
        dbconnect.commit()
        dbconnect.close()
        channel = self.client.get_channel(int(warn_id))
        embed = discord.Embed(title="User Warned!", description="**{0}** was warned by **{1}** ! They now have **{2}** warnings!".format(member, ctx.message.author, allWarnings, color=1752220))
        await channel.send(embed=embed)

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def warnings(self, ctx, member: discord.Member):
        allWarnings = 0
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        records = cursor.execute("SELECT username, warnings FROM warnings WHERE username = ?", [str(member)]).fetchall()
        for row in records:
            allWarnings = row[1]
        dbconnect.close()
        await ctx.send("The user has **{0}** warnings in total".format(allWarnings))

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def clearwarnings(self, ctx, member: discord.Member):
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        cursor.execute("SELECT username, warnings FROM warnings WHERE username = ?", [str(member)])
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM warnings WHERE username = ?", [str(member)])
            await ctx.send("Warnings Cleared!")
        else:
            await ctx.send("User already has no warnings!")
        dbconnect.commit()
        dbconnect.close()

    @client.command()
    async def report(self, ctx, member: discord.Member, reason):
        channel = self.client.get_channel(int(report_id))
        embed = discord.Embed(title="Report Submitted!", description="**{0}** was reported by **{1}** at **{2}** for **{3}** in channel **{4}**".format(member, ctx.message.author, ctime(), reason, ctx.channel, color=CDC311))
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))
