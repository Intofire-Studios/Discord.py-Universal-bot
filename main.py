from discord.ext import commands
from modules import cfgCreate
import os
from os import system
from tabulate import tabulate

system("cls")

path = 'settings.ini'

if os.path.exists('settings.ini') == False:
    cfgCreate.cfgCreate(path)

from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    text = "\033[32m {}" .format("Logged in as " + bot.user.name)
    table = [[text]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ", sep='\n')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])