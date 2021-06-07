from discord.ext import commands
from modules import cfgCreate
import os

path = 'settings.ini'

if os.path.exists('settings.ini') == False:
    cfgCreate.cfgCreate(path)

from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    print("Bot is running...")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])