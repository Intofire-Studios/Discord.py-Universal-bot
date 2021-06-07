from discord.ext import commands
import os
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])