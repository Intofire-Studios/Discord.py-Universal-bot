import discord
from discord.ext import commands
from extensions.config.config import lang

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description=lang['polldc'], brief=lang['polldc'])
    async def poll(self, ctx, *, question=None):
        if question is None:
            await ctx.send(lang['notpoll'])
        pollEmbed = discord.Embed(title = lang['newpoll'], description = f"{question}")
        pollEmbed.set_footer(text = lang['pollgivenby'] + f" {ctx.author}", icon_url = ctx.author.avatar_url)
        pollEmbed.timestamp = ctx.message.created_at 
        await ctx.message.delete()
        poll_msg = await ctx.send(embed = pollEmbed)

        await poll_msg.add_reaction("⬆️")
        await poll_msg.add_reaction("⬇️")


def setup(bot):
    bot.add_cog(Poll(bot))