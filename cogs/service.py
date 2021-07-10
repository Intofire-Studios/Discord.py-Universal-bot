import discord
from discord.ext import commands
from extensions.config.config import settings, lang
import os
from time import time
import extensions.versionhandler.vercheck as ver

class Service(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=lang['pongdc'], brief=lang['pongdc'])
    async def ping(self, ctx):
        st = time()
        message = await ctx.send(lang['pong'] + " :ping_pong: " + lang['latency'] + f" {self.bot.latency*1000:,.0f} ms.")
        end = time()
        await message.edit(content=lang['pong'] + " :ping_pong: " + lang['latency'] + f" {self.bot.latency*1000:,.0f} ms. " + lang['response'] + f" {(end-st)*1000:,.0f} ms.")

    @commands.command(description=lang['avatardc'], brief=lang['avatardc'])
    async def avatar(self, ctx):
        author = ctx.message.author
        
        embed = discord.Embed(title=lang['avatar'] + f" {author}"[:-5],
                                color=discord.Color.dark_gray())
        link = author.avatar_url
        embed.set_image(url = link)

        await ctx.send(embed=embed)

    @commands.command(description=lang['hellodc'], brief=lang['hellodc'])
    async def hello(self, ctx):
        author = ctx.message.author
        await ctx.send(lang['hello'] + f', {author.mention}!')

    @commands.command(pass_context=True, description=lang['saydc'], brief=lang['saydc'])
    async def say(self, ctx, arg):
        await ctx.send(arg)

    @commands.command(description=lang['shutdowndc'], brief=lang['shutdowndc'])
    async def shutdown(self, ctx):
        if ctx.author.id == int(settings['adminid']):
            await ctx.send(lang['shutdown'])
            ver.update()
            os.abort()
        else:
            await ctx.send(lang['notenoughrights'])

def setup(bot):
    bot.add_cog(Service(bot))
