import discord
from discord.ext import commands

client = commands.Bot(command_prefix='Bot')

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events
    #Sends a console message as the Bot ID to login to
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Online!')

    @client.event
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send('Please ensure you are permitted to use this command!')

    @client.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
    
    @client.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @client.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
    
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=int):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.send('Please specify an amount of messages to delete!')

def setup(client):
    client.add_cog(Moderation(client))