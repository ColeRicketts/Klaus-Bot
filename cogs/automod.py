import discord
from discord.ext import commands
import sqlite3
import json
client = commands.Bot(command_prefix='!')

with open('config.json') as configFile:
    data = json.load(configFile)
    for value in data["server_details"]:
        automod_id = value['automod_id']


class Automod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    @client.event
    async def on_ready(self):
        print('Automod Online!')

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
                    embed = discord.Embed(title="Automod!", description="**{0}** was reported by automod for language! ORIGINAL MESSAGE: **{1}**".format(message.author, message.content, color=0xff00f6))
                    await channel.send(embed=embed)

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
        else:
            await ctx.send("Word not banned already!")
        dbconnect.commit()
        dbconnect.close()


def setup(client):
    client.add_cog(Automod(client))
