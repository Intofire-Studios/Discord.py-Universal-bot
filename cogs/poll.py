import discord
from discord.ext import commands
from extensions.config.config import settings

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    commandd = commands.Bot(command_prefix=settings['prefix'])

    @commandd.command(description="Creates a poll", brief="Creates a poll")
    async def poll(self, ctx, *, question=None):
        if question is None:
            await ctx.send("Please write a poll!")
        icon_url = ctx.author.avatar_url 
        pollEmbed = discord.Embed(title = "New Poll!", description = f"{question}")
        pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
        pollEmbed.timestamp = ctx.message.created_at 
        await ctx.message.delete()
        poll_msg = await ctx.send(embed = pollEmbed)

        await poll_msg.add_reaction("⬆️")
        await poll_msg.add_reaction("⬇️")


def setup(bot):
    bot.add_cog(Poll(bot))