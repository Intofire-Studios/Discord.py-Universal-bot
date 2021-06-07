from discord.ext import commands

class Service(commands.Cog):
    def __init__(self, bot):
        def __init__(self,bot):
            self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!')

    @commands.command(description="Just hello")
    async def hello(self, ctx):
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')
    
    @commands.command(pass_context=True)
    async def test(self, ctx, arg):
        await ctx.send(arg)

def setup(bot):
    bot.add_cog(Service(bot))