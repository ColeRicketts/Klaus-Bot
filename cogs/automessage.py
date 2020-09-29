import discord
from discord.ext import commands
from time import ctime
import json
client = commands.Bot(command_prefix='!')

with open('config.json') as configFile:
    data = json.load(configFile)
    for value in data["server_details"]:
        welcome_id = value['welcome_id']


class Moderation(commands.Cog):
    def __init__(self, clientValue):
        self.client = clientValue

    @commands.Cog.listener()
    async def on_ready(self):
        print('Automessage Online!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(int(welcome_id))
        embedVar = discord.Embed(title="USER JOINED:", description="User: **{0}**".format(member.mention),
                                 color=0x979c9f)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.set_footer(text="Welcome to the server!")
        await channel.send(embed=embedVar)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(int(welcome_id))
        embedVar = discord.Embed(title="USER LEFT:", description="User: **{0}**".format(member.mention),
                                 color=0x979c9f)
        embedVar.add_field(name="Time:", value="**{0}**".format(ctime()), inline=True)
        embedVar.set_footer(text="Goodbye!")
        await channel.send(embed=embedVar)


def setup(clientValue):
    client.add_cog(Moderation(clientValue))
