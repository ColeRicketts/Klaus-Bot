from discord.ext import commands
class Automod(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Automod(client))