import discord
from discord.ext import commands
from time import sleep
client = commands.Bot(command_prefix='!')

alphabetReactions = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"]

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll Online!')

    @client.command()
    async def rating(self, ctx, *, content):
        embedVar = discord.Embed(title="Rate: **{0}**".format(content), description="Give this a rating from 1 to 10! A-J is equal to 1-10!", color=0x9b59b6)
        embedVar.add_field(name="Called By:", value="**{0}**".format(ctx.author.mention), inline=False)
        message = await ctx.send(embed=embedVar)
        await message.add_reaction("🇦")
        await message.add_reaction("🇧")
        await message.add_reaction("🇨")
        await message.add_reaction("🇩")
        await message.add_reaction("🇪")
        await message.add_reaction("🇫")
        await message.add_reaction("🇬")
        await message.add_reaction("🇭")
        await message.add_reaction("🇮")
        await message.add_reaction("🇯")

    @client.command()
    async def truefalse(self, ctx, *, content):
        embedVar = discord.Embed(title="T or F: **{0}**".format(content),description="Is it true or false?", color=0x9b59b6)
        embedVar.add_field(name="Called By:", value="**{0}**".format(ctx.author.mention), inline=False)
        message = await ctx.send(embed=embedVar)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

    @client.command()
    async def poll(self, ctx, *, content):
        itemCount = 0
        splitMessage = content.split(";")
        pollTitle = splitMessage[0]
        embedVar = discord.Embed(title="Pick: **{0}**".format(pollTitle), description="Pick an option!", color=0x9b59b6)
        for i in splitMessage:
            if i == pollTitle:
                pass
            else:
                embedVar.add_field(name="Option {0}:".format(alphabetReactions[itemCount]), value="{0}".format(i), inline=True)
            itemCount += 1
        embedVar.add_field(name="Called By:", value="**{0}**".format(ctx.author.mention), inline=True)
        message = await ctx.send(embed=embedVar)
        itemCount = 0
        for i in splitMessage:
            if i == pollTitle:
                 pass
            else:
                await message.add_reaction(str(alphabetReactions[itemCount]))
                itemCount += 1
        sleep(10)
        await ctx.send("Done0")



def setup(client):
    client.add_cog(Moderation(client))