import discord
from discord.ext import commands
import youtube_dl
from dotenv import load_dotenv
import asyncio

load_dotenv()


class music(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def nc():
    pass

  @commands.command()
  async def join(self, ctx):
    print("Joined")
    if ctx.author.voice is None:
      return await ctx.send("You're not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
    
  @commands.command()
  async def play(self,ctx,url):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}  
    YDL_OPTIONS = {'format':"bestaudio"}
    voice = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      voice.play(source)
            
  @commands.command()
  async def pause(self,ctx):
    await ctx.voice_client.pause()
    await ctx.send("Paused")
        
  @commands.command()
  async def resume(self,ctx):
    await ctx.voice_client.resume()
    await ctx.send("Resume")

  @commands.command()
  async def blank():
    pass

def setup(client):
  client.add_cog(music(client))