import discord
from discord.ext import commands
from extensions.config.config import settings, lang
import os
from time import time
import extensions.versionhandler.vercheck as ver

class Service(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Says "Pong"', brief='Says "Pong"')
    async def ping(self, ctx):
        st = time()
        message = await ctx.send(f"Pong! :ping_pong: DWSP latency: {self.bot.latency*1000:,.0f} ms.")
        end = time()
        await message.edit(content=f"Pong! :ping_pong: DWSP latency: {self.bot.latency*1000:,.0f} ms. Response time: {(end-st)*1000:,.0f} ms.")

    @commands.command(description="Shows an avatar", brief="Shows an avatar")
    async def avatar(self, ctx):
        author = ctx.message.author
        
        embed = discord.Embed(title=f"Аватар {author}"[:-5],
                                color=discord.Color.dark_gray())
        link = author.avatar_url
        embed.set_image(url = link)

        await ctx.send(embed=embed)

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
            await ctx.send(lang['shutdown'])
            ver.update()
            os.abort()
        else:
            await ctx.send(lang['notenoughrights'])

def setup(bot):
    bot.add_cog(Service(bot))
