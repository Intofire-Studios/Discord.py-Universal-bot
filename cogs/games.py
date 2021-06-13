import random

from discord.ext import commands


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        description="Gives a random number between 1 and 100",
        brief="Gives a random number between 1 and 100")
    async def roll(self, ctx):
        n = random.randrange(1, 100)
        await ctx.send(n)

    @commands.command(
        description="Random number between 1 and 6",
        brief="Random number between 1 and 6")
    async def dice(self, ctx):
        num = random.randrange(1, 6)
        await ctx.send(num)

    @commands.command(
        description="Either Heads or Tails",
        brief="Either Heads or Tails")
    async def coin(self, ctx):
        num = random.randint(0, 1)
        await ctx.send("Heads" if num == 1 else "Tails")


def setup(bot):
    bot.add_cog(Games(bot))
