import discord
from discord.ext import commands
from extensions.config.config import settings


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    commandd = commands.Bot(command_prefix=settings['prefix'])
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("This is not a command.")

def setup(bot):
    bot.add_cog(Events(bot))