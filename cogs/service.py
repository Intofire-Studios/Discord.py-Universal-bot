from discord.ext import commands

class Service(commands.Cog):
    def __init__(self, bot):
        def __init__(self,bot):
            self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong :ping_pong:!')

    @commands.command()
    async def avatar(ctx):
        author = ctx.message.author
        #link = {author.avatar_url_as()}

        #embed = discord.Embed(color = 0x002fff, title = 'Аватар пользователя')
        #embed.set_image(url = link)
        #await ctx.send(embed = embed)

        await ctx.send(f'{author.avatar_url_as()}')

    @commands.command(description="Just hello")
    async def hello(self, ctx):
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')
    
    @commands.command(pass_context=True)
    async def say(self, ctx, arg):
        await ctx.send(arg)

def setup(bot):
    bot.add_cog(Service(bot))