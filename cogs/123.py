import discord
from discord.ext import commands
from extensions.config.config import lang
from easy_password_generator import PassGen

class generaror(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    pwo = PassGen()
    pwo.generate()


def setup(bot):
    bot.add_cog(generaror(bot))
