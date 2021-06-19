import json
import discord
from discord.ext import commands
import requests

class Pics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Gives a random fox picture", brief="fox")
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title='Random fox')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)

    @commands.command(
        description="Gives a random cat picture",
        brief="cat")
    async def cat(self, ctx):
        response = requests.get('https://some-random-api.ml/img/cat')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0x808080, title='Random cat')
        embed.set_image(url=json_data['link'])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Pics(bot))
