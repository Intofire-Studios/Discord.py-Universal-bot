import asyncio
import discord
from discord.ext import commands
from discord.utils import get
import requests
import youtube_dl
from extensions.config.config import lang

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.song_queue = []
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    @staticmethod
    def parse_duration(duration):
        m, s = divmod(duration, 60)
        h, m = divmod(m, 60)
        return f'{h:d}:{m:02d}:{s:02d}'

    @staticmethod
    def search(author, arg):
        ydl_opts = {
            'quiet': 'True',
            'format': 'bestaudio',
            'noplaylist': 'True'
            }
        try:
            requests.get("".join(arg))
        except:
            arg = " ".join(arg)
        else:
            arg = "".join(arg)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]

        embed = (discord.Embed(title='🎵 ' + lang['nowplaying'], description=f"{info['title']}", color=discord.Color.blue())
                 .add_field(name=lang['duration'], value=Music.parse_duration(info['duration']))
                 .add_field(name=lang['reqby'], value=author)
                 .add_field(name=lang['uploader'], value=f"[{info['uploader']}]({info['channel_url']})")
                 .add_field(name=lang['url'], value=f"[Link to the video]({info['webpage_url']})")
                 .set_thumbnail(url=info['thumbnail']))

        return {'embed': embed, 'source': info['formats'][0]['url'], 'title': info['title'], 'duration': info['duration']}

    def play_next(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if len(self.song_queue) > 1:
            del self.song_queue[0]
            voice.play(
                discord.FFmpegPCMAudio(self.song_queue[0]['source'], **self.FFMPEG_OPTIONS),
                after=lambda e: self.play_next(ctx))
            voice.is_playing()
            asyncio.run_coroutine_threadsafe(
                ctx.send(embed=self.song_queue[0]['embed'], delete_after=self.song_queue[0]['duration']), self.bot.loop)
        else:
            asyncio.run_coroutine_threadsafe(voice.disconnect(), self.bot.loop)

    @commands.command(brief='play [url/key_words]', description='Plays youtube videos')
    async def play(self, ctx, *arg):
        channel = ctx.message.author.voice.channel
        await ctx.channel.purge(limit=1)

        if channel:
            voice = get(self.bot.voice_clients, guild=ctx.guild)
            song = self.search(ctx.author.mention, arg)
            self.song_queue.append(song)

            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()

            if not voice.is_playing():
                voice.play(
                    discord.FFmpegPCMAudio(self.song_queue[0]['source'], **self.FFMPEG_OPTIONS),
                    after=lambda e: self.play_next(ctx))
                voice.is_playing()
                await ctx.send(embed=song['embed'], delete_after=song['duration'])
            else:
                await ctx.send(
                    ":white_check_mark: " + lang['track'] + f" **{song['title']}** " + lang['trackadded'] + f" ({len(self.song_queue)-1} " + lang['togo'] + ")",
                    delete_after=self.song_queue[0]['duration'])

    @commands.command(aliases=['q'], brief="queue", description="Queue")
    async def queue(self, ctx):
        await ctx.channel.purge(limit=1)
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        embed = discord.Embed(color=discord.Color.blue(), title="⏱️ " + lang['queue'])
        if voice and voice.is_playing():
            for i in self.song_queue:
                if self.song_queue.index(i) == 0:
                    embed.add_field(name='**🔴 ' + lang['nowplaying'] + '**', value=f"{i['title']}", inline=False)
                else:
                    embed.add_field(
                        name=f'**🎵 Track n°{self.song_queue.index(i)} :**', value=f"{i['title']}", inline=False)
            await ctx.send(embed=embed, delete_after=self.song_queue[0]['duration'])
        else:
            await ctx.send("❌ " + lang['notplaying'], delete_after=5.0)

    @commands.command(brief='pause', description='Pauses or resumes the current song')
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        await ctx.channel.purge(limit=1)
        if voice and voice.is_connected():
            if voice.is_playing():
                await ctx.send('⏸️ ' + lang['pause'], delete_after=5.0)
                voice.pause()
            else:
                await ctx.send('⏯️ ' + lang['resume'], delete_after=5.0)
                voice.resume()
        else:
            await ctx.send("❌ " + lang['notconnected'], delete_after=5.0)

    @commands.command(aliases=['s', 'pass'], brief='skip', description='Skips the current song')
    async def skip(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        await ctx.channel.purge(limit=1)
        if voice and voice.is_playing():
            await ctx.send('⏭️ ' + lang['skip'], delete_after=5.0)
            voice.stop()
        else:
            await ctx.send("❌ " + lang['notplaying'], delete_after=5.0)


def setup(bot):
    bot.add_cog(Music(bot))
