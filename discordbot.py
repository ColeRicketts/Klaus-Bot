# Run this file to start the bot
import os
import json
from discord.ext import commands
client = commands.Bot(command_prefix='!')

with open('config.json') as configFile:
    data = json.load(configFile)
    for value in data["server_details"]:
        bot_token = value['bot_token']


@client.event
async def on_ready():
    print('Bot is ready (client)')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Ensure to give all required arguments. Type !help <commandName> to see the requirements!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Ensure you have permission for this!')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command doesn't exist!")


@client.command()
@commands.has_permissions()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(description=f'Loaded Extension {extension}')
    await ctx.send(embed=embed)
    print(f'Loaded Extention {extension}')
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(description=f'Unloaded Extension {extension}')
    await ctx.send(embed=embed)
    print(f'Unloaded Extention {extension}')

@client.command()
async def reload(extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(description=f'Reloaded Extension {extension}')
    await ctx.send(embed=embed)
    print(f'Reloaded Extention {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(bot_token)
