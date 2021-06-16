import os
from os import system

import discord
from discord.ext import commands

from extensions.config import cfgCreate

from tabulate import tabulate

system("cls")

path = 'settings.ini'

if not os.path.exists('settings.ini'):
    cfgCreate.cfgcreate(path)

from extensions.config.config import settings

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())


@bot.event
async def on_ready():
    if settings['status'] == "online":
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(settings['playing']))
    elif settings['status'] == "idle":
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(settings['playing']))
    elif settings['status'] == "dnd":
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(settings['playing']))
    elif settings['status'] == "insivible":
        await bot.change_presence(status=discord.Status.invisible, activity=discord.Game(settings['playing']))

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
