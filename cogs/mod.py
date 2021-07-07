import discord
from discord.ext import commands
from extensions.config.config import lang

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="kick user", brief="kick [ping/ID]")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} " + lang['kickby'] + f" {ctx.author.mention}. [{reason}]")

    @commands.command(description="ban user", brief="ban [ping/ID]")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} " + lang['banby'] + f" {ctx.author.mention}. [{reason}]")
    
    @commands.command(description="unban user", brief="unban [ping/ID]")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} " + lang['unbanby'] + f" {ctx.author.mention}")

    @commands.command(description="clear messages", brief="clear [number]")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} " + lang['msgdelete'])


def setup(bot):
    bot.add_cog(Moderation(bot))
