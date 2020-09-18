'''
import discord
from discord.ext import commands
from youtube_search import YoutubeSearch

client = commands.Bot(command_prefix='!')

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    @client.event
    async def on_ready(self):
        print("Voice online!")

    @commands.Cog.listener()
    @client.event
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Ensure to give all required arguments. Type !help <commandname> to see the requirements!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Ensure you have permission for this!')
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("This command doesn't exist!")

    @client.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @client.command(pass_context=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @client.command()
    async def play(self, ctx, query):
        videos = YoutubeSearch(query, max_results=1).to_dict()
        option = videos[0]
        link = ('https://www.youtube.com/watch?v='+option['id'])
        server = ctx.message.guild
        voice_client = ctx.guild.voice_client(server)
        player = await voice_client.create_ytdl_player(link)
        players[server.id] = player
        player.start()


def setup(client):
    client.add_cog(Voice(client))
'''
