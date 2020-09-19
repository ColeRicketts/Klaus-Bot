import discord
from discord.ext import commands
client = commands.Bot(command_prefix='!')

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll Online!')

def setup(client):
    client.add_cog(Moderation(client))