import os
from os import system
from sys import platform
import discord
from discord.ext import commands

from extensions.config.cfgCreate import cfgcreate

from tabulate import tabulate

if platform in ["linux", "linux2"]:
    system("reset")
elif platform == "win32":
    system("cls")

path = 'settings.ini'

if not os.path.exists('settings.ini'):
    cfgcreate(path)

from extensions.config.config import settings, lang

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())

@bot.event
async def on_ready():
    if settings['status'] == "online":
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(settings['playing']))
    elif settings['status'] == "idle":
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(settings['playing']))
    elif settings['status'] == "dnd":
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(settings['playing']))
    elif settings['status'] == "invisible":
        await bot.change_presence(status=discord.Status.invisible, activity=discord.Game(settings['playing']))

    text = "\033[32m {}" .format(lang['login'] + " " + bot.user.name)
    table = [[text]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ")
    pref = "\033[31m {}" .format(lang['prefix'] + ": " + settings['prefix'])
    table = [[pref]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ")
    stat = "\033[33m {}" .format(lang['status'] + ": " + settings['status'])
    table = [[stat]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ")
    pl = "\033[34m {}" .format(lang['playing'] + " " + settings['playing'])
    table = [[pl]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ", sep='\n')


@bot.command(description=lang['unloaddc'], brief=lang['unloadbrief'])
async def unload(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(lang['cogunload'])
    else:
        await ctx.send(lang['notenoughrights'])


@bot.command(description=lang['loaddc'], brief=lang['loadbrief'])
async def load(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(lang['cogload'])
    else:
        await ctx.send(lang['notenoughrights'])


@bot.command(description=lang['reloaddc'], brief=lang['reloadbrief'])
async def reload(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(lang['cogreload'])
    else:
        await ctx.send(lang['notenoughrights'])

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])
