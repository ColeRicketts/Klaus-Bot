import discord
from discord.ext import commands
import youtube_dl
from youtube_search import YoutubeSearch
import os
client = commands.Bot(command_prefix='!')

ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'music_download1.mp3',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
}

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Music Online!')

    @client.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @client.command()
    async def join(self, ctx):
        await ctx.author.voice.channel.connect()

    @client.command()
    async def play(self, ctx, *, message):
        song_there = os.path.isfile(r"./music_download1.mp3")
        try:
            if song_there:
                os.remove(r"./music_download1.mp3")
        except PermissionError:
            await ctx.send("Song already playing!")
        results = YoutubeSearch(str(message), max_results=1).to_dict()
        id = results[0].get("id")
        id = "https://www.youtube.com/watch?v="+str(id)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([id])
        voice = await ctx.author.voice.channel.connect()
        await voice.play(discord.FFmpegPCMAudio(r"./music_download1.mp3"))
        await ctx.send("Playback Started!")

def setup(client):
    client.add_cog(Music(client))