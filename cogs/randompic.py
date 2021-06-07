import discord
from discord.ext import commands
import json
import requests

class Pics(commands.Cog):
    def __init__(self, bot):
        def __init__(self,bot):
            self.bot = bot

    @commands.command()
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)

        embed = discord.Embed(color = 0xff9900, title = 'Random Fox')
        embed.set_image(url = json_data['link'])
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Pics(bot))