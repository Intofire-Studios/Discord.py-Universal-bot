from config import settings

from discord.ext import commands


class Service(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Says "Pong"', brief='Says "Pong"')
    async def ping(self, ctx):
        await ctx.send('Pong :ping_pong:!')

    @commands.command(description="Shows an avatar", brief="Shows an avatar")
    async def avatar(self, ctx):
        author = ctx.message.author

        # Я просто оставлю это здесь: я хотел, чтобы аватарка показывалась в Embed, а не в обычном тексте.

        # link = {author.avatar_url_as()}

        # embed = discord.Embed(color = 0x002fff, title = 'Аватар пользователя')
        # embed.set_image(url = link)
        # await ctx.send(embed = embed)

        await ctx.send(f'{author.avatar_url_as()}')

    @commands.command(description="Just hello", brief="Just hello")
    async def hello(self, ctx):
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')

    @commands.command(pass_context=True, description="Will repeat the text", brief="Will repeat the text")
    async def say(self, ctx, arg):
        await ctx.send(arg)

    @commands.command(description="Shutdown the bot", brief="Shutdown the bot")
    async def shutdown(self, ctx):
        if ctx.author.id == int(settings['adminid']):
            await ctx.send('Shutting down... :wave:')
            await ctx.bot.close()
        else:
            await ctx.send("You don't have enough rights to exec this command.")


def setup(bot):
    bot.add_cog(Service(bot))
