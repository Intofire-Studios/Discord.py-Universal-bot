import json

import discord
from discord.ext import commands

from extensions.config.config import settings


class Service(commands.Cog):

    commandd = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Says "Pong"', brief='Says "Pong"')
    async def ping(self, ctx):
        await ctx.send('Pong :ping_pong:!')

    @commands.command(description="Shows an avatar", brief="Shows an avatar")
    async def avatar(self, ctx):
        author = ctx.message.author

        # Я просто оставлю это здесь: я хотел, чтобы аватарка показывалась в Embed, а не в обычном тексте.

        # link = {author.avatar_url_as()}

        # embed = discord.Embed(color = 0x002fff, title = 'Аватар пользователя')
        # embed.set_image(url = link)
        # await ctx.send(embed = embed)

        await ctx.send(f'{author.avatar_url_as()}')

    @commands.command(description="Just hello", brief="Just hello")
    async def hello(self, ctx):
        author = ctx.message.author
        await ctx.send(f'Hello, {author.mention}!')

    @commands.command(pass_context=True, description="Will repeat the text", brief="Will repeat the text")
    async def say(self, ctx, arg):
        await ctx.send(arg)

    @commands.command(description="Shutdown the bot", brief="Shutdown the bot")
    async def shutdown(self, ctx):
        if ctx.author.id == int(settings['adminid']):
            await ctx.send('Shutting down... :wave:')
            await ctx.bot.close()
        else:
            await ctx.send("You don't have enough rights to execute this command.")

    @commandd.event
    async def on_raw_reaction_add(self, payload):

        if not payload.member.bot:
            with open('extensions/json/reactrole.json') as react_file:
                data = json.load(react_file)
                for xxx in data:
                    if xxx['emoji'] == payload.emoji.name:
                        role = discord.utils.get(commands.get_guild(
                            payload.guild_id).roles, id=xxx['role_id'])

                        await payload.member.add_roles(role)

    @commandd.event
    async def on_raw_reaction_remove(self, payload):
        with open('extensions/json/reactrole.json') as react_file:
            data = json.load(react_file)
            for xxx in data:
                if xxx['emoji'] == payload.emoji.name:
                    role = discord.utils.get(commands.get_guild(
                        payload.guild_id).roles, id=xxx['role_id'])
                    await commands.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

    @commands.command()
    @commands.has_permissions(administrator=True, manage_roles=True)
    async def reactrole(self, ctx, emoji, role: discord.Role, *, message):

        emb = discord.Embed(description=message)
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction(emoji)

        with open('extensions/json/reactrole.json') as json_file:
            data = json.load(json_file)

            new_react_role = {
                'role_name': role.name,
                'role_id': role.id,
                'emoji': emoji,
                'message_id': msg.id}

            data.append(new_react_role)

        with open('extensions/json/reactrole.json', 'w') as f:
            json.dump(data, f, indent=4)


def setup(bot):
    bot.add_cog(Service(bot))
