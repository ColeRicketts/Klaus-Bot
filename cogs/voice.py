import discord
from discord.ext import commands

client = commands.Bot(command_prefix='Bot')

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    @client.event
    async def on_ready(self):
        print("Voice online!")  

    @client.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    @client.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(Voice(client))