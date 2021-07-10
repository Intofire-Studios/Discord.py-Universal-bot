import random
from discord.ext import commands

from extensions.config.config import lang

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        description=lang['rolldc'],
        brief=lang['rolldc'])
    async def roll(self, ctx):
        num = random.randrange(1, 100)
        await ctx.send(num)

    @commands.command(
        description=lang['dicedc'],
        brief=lang['dicedc'])
    async def dice(self, ctx):
        num = random.randrange(1, 6)
        await ctx.send(num)

    @commands.command(
        description=lang['coindc'],
        brief=lang['coindc'])
    async def coin(self, ctx):
        num = random.randint(0, 1)
        await ctx.send(lang['coinheads'] if num == 1 else lang['cointails'])


def setup(bot):
    bot.add_cog(Games(bot))
