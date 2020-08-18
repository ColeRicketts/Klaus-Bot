import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

# Assigns client to the command prefix of Bot
client = commands.Bot(command_prefix='Bot')
status = cycle(['Idling in the system RAM', 'discordbotmaster.py on VS code', 'slowly reconsidering my life'])

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready (client)')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('NjkyMDEwNDY4NzEzNDMxMDUw.XnoS-A.KCL0m2gsOpFE1f7Ud4oYIbD-sRY')