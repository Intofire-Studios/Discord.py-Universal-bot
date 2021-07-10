import discord
from discord.ext import commands
from extensions.config.config import lang


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandNotFound):
            msg4 = lang['msgcmdnotfound'] + "!"
            em16 = discord.Embed(title="**" + lang['errorblock'] + "**",
                             color=discord.Color.red())
            em16.add_field(name="__" + lang['cmdnotfound'] + ":__", value=msg4)
            await ctx.send(embed=em16)
        if isinstance(error, commands.CommandOnCooldown):
            msg = lang['msgslowmodeerror'] + ' {:.2f}s.'.format(
                error.retry_after) 
            em13 = discord.Embed(title="**" + lang['errorblock'] + "**",
                                color=discord.Color.red())
            em13.add_field(name="__" + lang['slowmodeerror'] + ":__", value=msg) 
            await ctx.send(embed=em13)
        if isinstance(error, commands.MissingRequiredArgument):
            msg2 = lang['msgmissingarguments'] + "!"
            em14 = discord.Embed(title=lang['errorblock'], color=discord.Color.red())
            em14.add_field(name="__" + lang['missingarguments'] + ":__", value=msg2)
            await ctx.send(embed=em14)
        if isinstance(error, commands.MissingPermissions):
            msg3 = lang['msgmissingpermissions'] + "!"
            em15 = discord.Embed(title="**" + lang['errorblock'] + "**",
                                color=discord.Color.red())
            em15.add_field(name="__" + lang['missingpermissions'] + ":__", value=msg3)
            await ctx.send(embed=em15)
        if isinstance(error, commands.CommandInvokeError):
            await ctx.channel.purge(limit=1)
            msg4 = "❌ " + lang['msgnotvoice'] + "!"
            em16 = discord.Embed(title="**" + lang['errorblock'] + "**",
                                color=discord.Color.red())
            em16.add_field(name="__" + lang['notvoice'] + ":__", value=msg4)
            await ctx.send(embed=em16, delete_after=5.0)

def setup(bot):
    bot.add_cog(Events(bot))