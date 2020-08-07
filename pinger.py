import discord
from discord.ext import commands

class Pinger(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events
    #Sends a console message as the Bot ID to login to
    @commands.Cog.listener()
    async def on_ready(self):
        print('Pinger Online!')
    
    #Commands
    #On recieving the command prefix+ping, responds with TestCommand
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Ping Recieved!')

def setup(client):
    client.add_cog(Pinger(client))