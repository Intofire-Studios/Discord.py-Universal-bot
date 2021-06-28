import os
from os import system
from sys import platform
import discord
from discord.ext import commands
import extensions.versionhandler.vercheck as ver

from extensions.config.cfgCreate import cfgcreate

from tabulate import tabulate

if platform in ["linux", "linux2"]:
    system("reset")
elif platform == "win32":
    system("cls")

path = 'settings.ini'

if not os.path.exists('settings.ini'):
    cfgcreate(path)

from extensions.config.config import settings

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())

ver.update()

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

    text = "\033[32m {}" .format("Logged in as " + bot.user.name)
    table = [[text]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ")
    pref = "\033[31m {}" .format("Prefix: " + settings['prefix'])
    table = [[pref]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ")
    stat = "\033[33m {}" .format("Status: " + settings['status'])
    table = [[stat]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ")
    pl = "\033[34m {}" .format("Playing: " + settings['playing'])
    table = [[pl]]
    print(tabulate(table, tablefmt='grid'), "\033[0m ", sep='\n')


@bot.command(description="Unload cogs", brief="unload [cog_name]")
async def unload(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Cog is unloaded...")
    else:
        await ctx.send("You don't have enough rights to execute this command.")


@bot.command(description="Load cogs", brief="load [cog_name]")
async def load(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cog is loaded...")
    else:
        await ctx.send("You don't have enough rights to execute this command.")


@bot.command(description="Reload cogs", brief="reload [cog_name]")
async def reload(ctx, extension):
    if ctx.author.id == int(settings['adminid']):
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Cog is reloaded...")
    else:
        await ctx.send("You don't have enough rights to execute this command.")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(settings['token'])
