import discord
from discord.ext import commands
import json
client = commands.Bot(command_prefix='!')

with open('config.json') as configFile:
    data = json.load(configFile)
    for value in data["server_details"]:
        announce_id = value['announcements_id']

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Announcement Online!')

    @client.command()
    @commands.has_permissions(manage_channels= True)
    async def announcetitle(self, ctx, *, title):
        global annctitle
        annctitle = title
        await ctx.send("Announcement Title Set!")

    @client.command()
    @commands.has_permissions(manage_channels=True)
    async def announcemessage(self, ctx, *, message):
        global anncmessage
        anncmessage = message
        await ctx.send("Announcement Message Set!")

    @client.command()
    @commands.has_permissions(manage_channels=True)
    async def announce(self):
        channel = self.client.get_channel(int(announce_id))
        embedVar = discord.Embed(title="**{0}**".format(annctitle), description="{0}".format(anncmessage), color=0xe91e63)
        await channel.send(embed=embedVar)

    @client.command()
    @commands.has_permissions(manage_channels=True)
    async def serverannounce(self, ctx):
        for channel in ctx.guild.text_channels:
            embedVar = discord.Embed(title="**{0}**".format(annctitle), description="{0}".format(anncmessage), color=0xe91e63)
            await channel.send(embed=embedVar)

    @client.command()
    @commands.has_permissions(manage_channels=True)
    async def everyoneannounce(self, ctx):
        channel = self.client.get_channel(int(announce_id))
        embedVar = discord.Embed(title="**{0}**".format(annctitle), description="{0}".format(anncmessage), colour=0xe91e63)

def setup(client):
    client.add_cog(Moderation(client))