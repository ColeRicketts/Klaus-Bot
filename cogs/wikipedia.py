import discord
from discord.ext import commands
import wikipedia

client = commands.Bot(command_prefix='!')

class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    @client.event
    async def on_ready(self):
        print("Wiki online!")


    @client.command()
    async def define(self, ctx):
        msg = ctx.message.content.split(" ")
        request = msg[1:]
        request = " ".join(request)
        error = None
        definition = wikipedia.summary(request, sentences=2, chars=1000, auto_suggest=True, redirect = True)
        search=discord.Embed(title="Wikipedia Result", description=definition, colour=discord.Colour.dark_green())
        await ctx.send(content=None, embed=search)


def setup(client):
    client.add_cog(Wikipedia(client))