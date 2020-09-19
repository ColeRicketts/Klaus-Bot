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
        mod_id = value['modaction_id']


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
        channel = self.client.get_channel(int(mod_id))
        embedVar = discord.Embed(title="USER KICKED", description="Issued by **{0}**".format(ctx.message.author), color=0x1abc9c)
        embedVar.add_field(name="User:", value="**{0}**".format(member.mention), inline=True)
        embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.add_field(name="Reason:", value="**{0}**".format(reason), inline=True)
        await channel.send(embed=embedVar)
        await ctx.send("User Kicked!")
    
    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        channel = self.client.get_channel(int(mod_id))
        embedVar = discord.Embed(title="USER BANNED", description="Issued by **{0}**".format(ctx.message.author), color=0x3498db)
        embedVar.add_field(name="User:", value="**{0}**".format(member.mention), inline=True)
        embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.add_field(name="Reason:", value="**{0}**".format(reason), inline=True)
        await channel.send(embed=embedVar)
        await ctx.send("User Banned!")


    @client.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                channel = self.client.get_channel(int(mod_id))
                embedVar = discord.Embed(title="USER UNBANNED", description="Issued by **{0}**".format(ctx.message.author), color=0x3498db)
                embedVar.add_field(name="User:", value="**{0}**".format(member.mention), inline=True)
                embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
                embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
                await channel.send(embed=embedVar)
                await ctx.send("User Unbanned!")

    @client.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, amount):
        await ctx.channel.edit(slowmode_delay=int(amount))
        embed = discord.Embed(title="Channel Slowed!", description="**{0}** was slowed by **{1}** for **{2}**s!".format(ctx.channel, ctx.message.author, int(amount), color=0x2ecc71))
        await ctx.send(embed=embed)
        channel = self.client.get_channel(int(mod_id))
        embedVar = discord.Embed(title="SLOWMODE ACTIVE", description="Issued by **{0}**".format(ctx.message.author), color=0x2ecc71)
        embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.add_field(name="Amount:", value="**{0}**s".format(int(amount)), inline=True)
        await channel.send(embed=embedVar)

    @client.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def unslow(self, ctx):
        await ctx.channel.edit(slowmode_delay=0)
        embed = discord.Embed(title="Channel Unslowed!", description="**{0}** was unslowed by **{1}** !".format(ctx.channel, ctx.message.author, color=0x2ecc71))
        await ctx.send(embed=embed)
        channel = self.client.get_channel(int(mod_id))
        embedVar = discord.Embed(title="SLOWMODE REMOVED", description="Issued by **{0}**".format(ctx.message.author), color=0x2ecc71)
        embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        await channel.send(embed=embedVar)

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        amount = amount+1
        await ctx.channel.purge(limit=amount)
        channel = self.client.get_channel(int(mod_id))
        embedVar = discord.Embed(title="MESSAGES CLEARED", description="Issued by **{0}**".format(ctx.message.author), color=0x2ecc71)
        embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.add_field(name="No. Cleared:", value="**{0}**".format(amount), inline=True)
        await channel.send(embed=embedVar)
        await ctx.send("Messages cleared!")

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
        embedVar = discord.Embed(title="MOD WARNING", description="Issued by **{0}**".format(ctx.message.author), color=0xe67e22)
        embedVar.add_field(name="User:", value="**{0}**".format(member.mention), inline=True)
        embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.add_field(name="Total:", value="**{0}** Warnings".format(allWarnings), inline=True)
        await channel.send(embed=embedVar)

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
            channel = self.client.get_channel(int(mod_id))
            embedVar = discord.Embed(title="WARNINGS CLEARED", description="Issued by **{0}**".format(ctx.message.author), color=0xe67e22)
            embedVar.add_field(name="User:", value="**{0}**".format(member.mention), inline=True)
            embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
            embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
            await channel.send(embed=embedVar)
            await ctx.send("Warnings Cleared!")
        else:
            await ctx.send("User already has no warnings!")
        dbconnect.commit()
        dbconnect.close()

    @client.command()
    async def report(self, ctx, member: discord.Member, reason):
        channel = self.client.get_channel(int(report_id))
        embedVar = discord.Embed(title="USER REPORTED", description="Issued by **{0}**".format(ctx.message.author), color=0xe67e22)
        embedVar.add_field(name="User:", value="**{0}**".format(member.mention), inline=True)
        embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.add_field(name="Reason:", value="**{0}**".format(reason), inline=True)
        await channel.send(embed=embedVar)
        await ctx.send("Reported to moderators!")


def setup(client):
    client.add_cog(Moderation(client))
