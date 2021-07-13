# Run this file to start the bot
import os
import json
from discord.ext import commands
from discord.ext.commands import AutoShardedBot as asb

class Klaus(asb):
    def __init__(self, load:bool=False):
        super().__init__(
            command_prefix="!",
            case_insensitive=True, # makes it so if you do !hElp the command is still recognized as !help
            # help_command=None, # uncomment this if you want the help command removed
        )

        with open('config.json') as configFile:
            self.data = json.load(configFile)
            for value in self.data["server_details"]:
                self.bot_token = value['bot_token']
        
        if load:
            print("Loading cogs:")
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        self.load_extension(f'cogs.{filename[:-3]}')
                        print(f"    Loaded '{filename}'")
                    except Exception as e:
                        print(str(e))
        
        @self.command()
        @commands.is_owner()
        async def load(self, ctx, extension):
            self.load_extension(f'cogs.{extension}')
            embed = discord.Embed(description=f'Loaded Extension {extension}')
            await ctx.send(embed=embed)
            print(f'Loaded Extention {extension}')

        @self.command()
        @commands.is_owner()
        async def unload(self, ctx, extension):
            self.unload_extension(f'cogs.{extension}')
            embed = discord.Embed(description=f'Unloaded Extension {extension}')
            await ctx.send(embed=embed)
            print(f'Unloaded Extention {extension}')

        @self.command()
        @commands.is_owner()
        async def reload(self, ctx, extension):
            self.reload_extension(f'cogs.{extension}') # make sure you REINSTALL discord.py if you dont have this feature. DO NOT UPGRADE IT BUT REINSTALL IT
            embed = discord.Embed(description=f'Reloaded Extension {extension}')
            await ctx.send(embed=embed)
            print(f'Reloaded Extention {extension}')

    async def on_connect(self): print("Connected")
    async def on_ready(self): print("Ready")
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Ensure to give all required arguments. Type !help <commandName> to see the requirements!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Ensure you have permission for this!')
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("This command doesn't exist!")

if __name__ == "__main__":
    bot = Klaus(load=True)
    bot.run(bot.bot_token)
