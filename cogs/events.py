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
            msg4 = "No command found!"
            em16 = discord.Embed(title="**Error Block**",
                             color=discord.Color.red())
            em16.add_field(name="__Command Not Found:__", value=msg4)
            await ctx.send(embed=em16)
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Still on cooldown, please try again in {:.2f}s.'.format(
                error.retry_after) 
            em13 = discord.Embed(title="**Error Block**",
                                color=discord.Color.red())
            em13.add_field(name="__Slowmode Error:__", value=msg) 
            await ctx.send(embed=em13)
        if isinstance(error, commands.MissingRequiredArgument):
            msg2 = "Please enter all the required arguments!"
            em14 = discord.Embed(title="Error Block", color=discord.Color.red())
            em14.add_field(name="__Missing Required Arguments:__", value=msg2)
            await ctx.send(embed=em14) #sending the embed
        if isinstance(error, commands.MissingPermissions):
            msg3 = "You are missing permissions to use that command!"
            em15 = discord.Embed(title="**Error Block**",
                                color=discord.Color.red())
            em15.add_field(name="__Missing Permissions:__", value=msg3)
            await ctx.send(embed=em15)
        if isinstance(error, commands.CommandInvokeError):
            await ctx.channel.purge(limit=1)
            msg4 = "❌ Connect to a voice channel first!"
            em16 = discord.Embed(title="**Error Block**",
                                color=discord.Color.red())
            em16.add_field(name="__Not in a voice channel:__", value=msg4)
            await ctx.send(embed=em16, delete_after=5.0)

def setup(bot):
    bot.add_cog(Events(bot))