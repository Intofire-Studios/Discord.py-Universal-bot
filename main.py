import os
from os import system

from config import settings

from discord.ext import commands

from modules import cfgCreate

from tabulate import tabulate

system("cls")

path = 'settings.ini'

if not os.path.exists('settings.ini'):
    cfgCreate.cfgcreate(path)

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.event
async def on_ready():
    text = "\033[32m {}" .format("Logged in as " + bot.user.name)
    table = [[text]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ")
    pref = "\033[31m {}" .format("Prefix: " + settings['prefix'])
    table = [[pref]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ", sep='\n')


@bot.command()  # TODO: Make a description
async def unload(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Cogs is unloaded...")
    else:
        await ctx.send("You don't have enough rights to execute this command.")


@bot.command()  # TODO: Make a description
async def load(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs is loaded...")
    else:
        await ctx.send("You don't have enough rights to execute this command.")


@bot.command()  # TODO: Make a description
async def reload(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs is reloaded...")
    else:
        await ctx.send("You don't have enough rights to exec this command.")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])
