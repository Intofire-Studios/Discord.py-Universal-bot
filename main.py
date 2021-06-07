import discord
from discord.ext import commands
from config import settings
import json
import requests

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')
@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)
@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(settings['token'])