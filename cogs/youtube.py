from youtube_search import YoutubeSearch

results = YoutubeSearch('search terms', max_results=10).to_json()

 # print(results)

# returns a json string
# GET ID FROM THING
########################################

results = YoutubeSearch('search terms', max_results=10).to_dict()

 # print(results)
# returns a dictionary,

from discord.ext import commands
class Youtube(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Youtube(client))

'''
voice = await voice_channel.connect()
voice.play(discord.FFmpegPCMAudio(URL)
'''