import discord
from discord.ext import commands
import sqlite3
import json
from time import ctime
client = commands.Bot(command_prefix='!')

with open('config.json') as configFile:
    data = json.load(configFile)
    for value in data["server_details"]:
        automod_id = value['automod_id']
        mod_id = value['modaction_id']


class Automod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    @client.event
    async def on_ready(self):
        print('Language Filter Online!')

    # Maybe use list from http://www.bannedwordlist.com/
    @commands.Cog.listener()
    async def on_message(self, message):
        message_content = message.content.strip().lower()
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        records = cursor.execute("SELECT word FROM bannedwords").fetchall()
        for row in records:
            if row[0] in message_content:
                if message.author.permissions_in(message.channel).manage_messages:
                    break
                else:
                    await message.channel.purge(limit=1)
                    await message.channel.send("Your message has been removed for: Censoring.")
                    channel = self.client.get_channel(int(automod_id))
                    embedVar = discord.Embed(title="LANGUAGE WARNING", description="Issued to **{0}**".format(message.author), color=0xe74c3c)
                    embedVar.add_field(name="User:", value="**{0}**".format(message.author.mention), inline=True)
                    embedVar.add_field(name="Channel:", value="**{0}**".format(message.channel.mention), inline=True)
                    embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
                    embedVar.add_field(name="Original Message:", value="**{0}**".format(message.content))
                    await channel.send(embed=embedVar)

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def banword(self, ctx, word):
        word = word.lower()
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        cursor.execute("SELECT word FROM bannedwords WHERE word = ?", (word,))
        result = cursor.fetchone()
        if result:
            await ctx.send("Word already banned!")
        else:
            cursor.execute('''INSERT INTO bannedwords(word) VALUES(?)''', (word,))
            await ctx.send("Word Banned!")
            channel = self.client.get_channel(int(mod_id))
            embedVar = discord.Embed(title="WORD BANNED", description="Issued by **{0}**".format(ctx.message.author), color=0xe74c3c)
            embedVar.add_field(name="Word:", value="**{0}**".format(word), inline=True)
            embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
            embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
            await channel.send(embed=embedVar)
        dbconnect.commit()
        dbconnect.close()

    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def unbanword(self, ctx, word):
        word = word.lower()
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        cursor.execute("SELECT word FROM bannedwords WHERE word = ?", (word,))
        result = cursor.fetchone()
        if result:
            cursor.execute("DELETE FROM bannedwords WHERE word = ?", (word,))
            await ctx.send("Word Unbanned!")
            channel = self.client.get_channel(int(mod_id))
            embedVar = discord.Embed(title="WORD UNBANNED", description="Issued by **{0}**".format(ctx.message.author), color=0xe74c3c)
            embedVar.add_field(name="Word:", value="**{0}**".format(word), inline=True)
            embedVar.add_field(name="Channel:", value="**{0}**".format(ctx.channel.mention), inline=True)
            embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
            await channel.send(embed=embedVar)
        else:
            await ctx.send("Word not banned already!")
        dbconnect.commit()
        dbconnect.close()


    @client.command()
    async def bannedwords(self, ctx):
        bannedTerms = "Banned Words: "
        dbconnect = sqlite3.connect('users.db')
        cursor = dbconnect.cursor()
        cursor.execute("SELECT word FROM bannedwords")
        result = cursor.fetchall()
        for row in result:
            bannedTerm = row[0]
            bannedTerms = bannedTerms + bannedTerm + ", "
        await ctx.send(bannedTerms)
        dbconnect.commit()
        dbconnect.close()


def setup(client):
    client.add_cog(Automod(client))
