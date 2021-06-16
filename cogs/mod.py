import discord
from discord import user
from discord.ext import commands
from discord.ext.commands.core import guild_only


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="kick user", brief="kick [ping/ID]")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}. [{reason}]")

    @commands.command(description="ban user", brief="ban [ping/ID]")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned by {ctx.author.mention}. [{reason}]")
    
    @commands.command(description="clear messages", brief="clear [number]") # TODO: Make a description
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} was unbanned by {ctx.author.mention}")

    @commands.command(description="clear messages", brief="clear [number]")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} messages got deleted.")


def setup(bot):
    bot.add_cog(Moderation(bot))
