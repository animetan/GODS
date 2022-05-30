from random import random
from threading import local
import time

import disnake
from disnake.ext import commands
from discord_components import DiscordComponents, Select, SelectOption, Button,ButtonStyle
from datetime import date, datetime, timedelta
import datetime
import sqlite3
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import CommandNotFound
from discord import FFmpegPCMAudio
from discord import Status
from asyncio import sleep
import random

import interactions

import DateTime
import asyncio
from PIL import Image, ImageFont, ImageDraw
import io
import requests
import io
from discord.ext import commands,tasks
from PIL import Image, ImageDraw, ImageFont
discordintents = discord.Intents(messages=True, guilds=True)
from io import BytesIO
client = discord.Client()
from dislash import SlashClient, ActionRow, Button
import ipc
import json
import requests
import timestamp
from discord.ext import commands
from discord_slash import SlashCommand, cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import os
from discord.ext import commands
from dislash import InteractionClient, SelectMenu, SelectOption
from dislash import SlashClient, ActionRow, Button
import interactions
from fuzzywuzzy import fuzz


intents = discord.Intents.all()
intents.members = True
intents.messages = True
client = InteractionClient


servers = [831071829170061326]

bot = interactions.Client(token="OTM4MDU4MDE2NDM4MjM5Mjgy.Gw-8uy.y2WAN-rIgzc8sxOQK6mgWVMNxOizVxs0k8yYD0")
client = commands.Bot(command_prefix = '-', intents=intents, help_command=None, case_insensitive=True)
slash = SlashCommand(client,sync_commands=True, sync_on_cog_reload=True, override_type = True)
DiscordComponents(client)








@bot.user_command(name="Hello user", scope=831071829170061326)
async def hello_user(ctx: interactions.CommandContext):
    await ctx.send(f"Hello, {ctx.target.username}#{ctx.target.discriminator}!")


@bot.user_command(name="трахнуть", scope=831071829170061326)
async def hello_member(ctx: interactions.CommandContext):
    member = interactions.Member(
        **await bot._http.get_member(ctx.guild_id, ctx.target.id), _client=bot._http
    )
    await ctx.send(
        f"Hello, {member.user.username if member.nick is None else member.nick}!"
    )


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')





@client.event
async def on_member_join(member):

	role = discord.utils.get(member.guild.roles, name = '神')
	await member.add_roles(role)
	channel=client.get_channel(860524616095105064)
	chanel = client.get_channel(938054056331599982)
	url = str(member.avatar_url)[:-10]
	url = requests.get(url, stream = True)
	avatar = Image.open(io.BytesIO(url.content))
	welcome = Image.open("hi.png")
	welcome = welcome.convert('RGBA')
	avatar = avatar.convert('RGBA')
	mask = Image.new('L',(1500,1500),0)
	draw = ImageDraw.Draw(avatar)
	idraw = ImageDraw.Draw(welcome)
	name = member.name
	tag = member.discriminator
	at = member.created_at
	server = member.guild.name
	idraw.rectangle((50, 50, 460, 460), fill = 'white')
	idraw.rectangle((50, 610, 1220, 490), fill = (64, 64, 64), outline = 'white', width = 10)
	idraw.rectangle((500, 340, 1220, 460), fill = (64, 64, 64), outline = 'white', width = 10)
	idraw.rectangle((500, 190, 1220, 310), fill = (64, 64, 64), outline = 'white', width = 10)
	headline = ImageFont.truetype('./assets/font.ttf', size=70)
	headline2 = ImageFont.truetype('./assets/font.ttf', size=70)
	idraw.text((640, 575), f'Ты по счёту:  {member.guild.member_count}',anchor="ms", font=headline, fill='#FFFFFF')
	idraw.text((530, 350), f'{name}#{tag}', font=headline2, fill='#FFFFFF')
	idraw.text((530, 200), "        g o d's", font=headline2, fill='#FFFFFF')
	draw.ellipse((0,0) + (1500,1500),fill = 255)
	avatar = avatar.resize((390,390))
	#avatar.putalpha(mask)
	welcome = welcome.crop((0, 0, 1280, 640))
	welcome.paste(avatar,(60,60),avatar)
	welcome.save('welcome.png')
	_buffer = io.BytesIO()
	welcome.save(_buffer,"png")
	_buffer.seek(0)
	role2 = discord.utils.get(member.guild.roles, name = 'ㅤㅤㅤㅤㅤ⤛Colors⤜ㅤㅤㅤㅤㅤㅤ')
	await member.add_roles(role2)
	role3 = discord.utils.get(member.guild.roles, name = 'None')
	await member.add_roles(role3)
	role4 = discord.utils.get(member.guild.roles, name = 'ㅤㅤㅤㅤㅤ⤛Roles⤜ㅤㅤㅤㅤㅤㅤㅤ')
	await member.add_roles(role4)
	await channel.send(file = discord.File(fp = _buffer,filename = f'{member.name}welcome.png'))
	await channel.send(f"{member.mention} добро пожаловать на сервер {member.guild.name}!")
	await chanel.edit(name = '𝐌𝐞𝐦𝐛𝐞𝐫𝐬:  {}'.format(channel.guild.member_count))
	#await member.send(file = discord.File(fp = _buffer,filename = f'{member.name}welcome.png'))
	await member.send(f"{member.mention} добро пожаловать на сервер {member.guild.name}!")
	guilds = await client.fetch_guilds(limit = None).flatten()
    
@client.event
async def on_member_remove(member):
	channel=client.get_channel(913524501617209364)
	chanel = client.get_channel(938054056331599982)
	url = str(member.avatar_url)[:-10]
	url = requests.get(url, stream = True)
	avatar = Image.open(io.BytesIO(url.content))
	welcome = Image.open("hi.png")
	welcome = welcome.convert('RGBA')
	avatar = avatar.convert('RGBA')
	mask = Image.new('L',(1500,1500),0)
	draw = ImageDraw.Draw(avatar)
	idraw = ImageDraw.Draw(welcome)
	name = member.name
	tag = member.discriminator
	at = member.created_at
	server = member.guild.name
	idraw.rectangle((50, 50, 460, 460), fill = 'white')
	idraw.rectangle((50, 610, 1220, 490), fill = (64, 64, 64), outline = 'white', width = 10)
	idraw.rectangle((500, 340, 1220, 460), fill = (64, 64, 64), outline = 'white', width = 10)
	idraw.rectangle((500, 190, 1220, 310), fill = (64, 64, 64), outline = 'white', width = 10)
	headline = ImageFont.truetype('./assets/font.ttf', size=70)
	headline2 = ImageFont.truetype('./assets/font.ttf', size=70)
	idraw.text((640, 575), f'Покинул нас',anchor="ms", font=headline, fill='#FFFFFF')
	idraw.text((530, 350), f'{name}#{tag}', font=headline2, fill='#FFFFFF')
	idraw.text((530, 200), "        g o d's", font=headline2, fill='#FFFFFF')
	draw.ellipse((0,0) + (1500,1500),fill = 255)
	avatar = avatar.resize((390,390))
	#avatar.putalpha(mask)
	welcome = welcome.crop((0, 0, 1280, 640))
	welcome.paste(avatar,(60,60),avatar)
	welcome.save('welcome.png')
	_buffer = io.BytesIO()
	welcome.save(_buffer,"png")
	_buffer.seek(0)
	await channel.send(file = discord.File(fp = _buffer,filename = f'{member.name}welcome.png'))
	await channel.send(f"{member.mention} Покинул наш прекрасный сервер: {member.guild.name}!")
	await chanel.edit(name = '𝐌𝐞𝐦𝐛𝐞𝐫𝐬:  {}'.format(channel.guild.member_count))
	#await member.send(file = discord.File(fp = _buffer,filename = f'{member.name}welcome.png'))
	guilds = await client.fetch_guilds(limit = None).flatten()


@client.event
async def on_ready():
       while True:
            await client.change_presence(activity=discord.Streaming(name="🎄prefix > -help", url="https://www.twitch.tv/degradki"))
            await sleep(15)
            await client.change_presence(activity=discord.Streaming(name="🎄 Я человек!🤔", url="https://www.twitch.tv/degradki"))
            await sleep(15)
            await client.change_presence(activity=discord.Streaming(name="🎄prefix > -help", url="https://www.twitch.tv/degradki"))
            await sleep(15)
            await client.change_presence(activity=discord.Streaming(name="🎄 Я умный бот?", url="https://www.twitch.tv/degradki"))
            await sleep(15)
            await client.change_presence(activity=discord.Streaming(name="🎄prefix > -help", url="https://www.twitch.tv/degradki"))
            await sleep(15)
            await client.change_presence(activity=discord.Streaming(name="🎄 Ну, типа я бот", url="https://www.twitch.tv/degradki"))
            await sleep(15)
            await client.change_presence(activity=discord.Streaming(name="🎄prefix > -help", url="https://www.twitch.tv/degradki"))
            await sleep(15)
            await client.change_presence(activity=discord.Streaming(name="🎄 Cлушаю музыку", url="https://www.twitch.tv/degradki"))
            await sleep(15)






         


@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title=":warning: Использована неизвестная команда.",description = "Пожалуйста, напишите `-help` для списка команд и соответствующего использования." , color=0xFF0080)
    await ctx.send(embed=embed, delete_after=10.0)
    print('Ошибка выполнения команды: ', error)
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Ошибка", description="Команда перезаряжается", color=0x00ff00)
        embed.set_footer(text="UsefullBot © 2022",icon_url="https://cdn.discordapp.com/avatars/975870441350643722/5fdc0ba8c4725d7118f80c828733ce5a.png?size=4096")
        embed.timestamp = datetime.datetime.utcnow()


    






  
@slash.slash(name="avatar",
             description="Аватар пользователя.",
             options=[
               create_option(
                 name="member",
                 description="Да, аватар",
                 option_type=6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=True
               )
             ])
async def avatar(ctx, *, member : discord.Member=None):
    if member == None:
      embed = discord.Embed(description = f'**Запросил: {ctx.author.name}**', icon_url=ctx.author.avatar_url,color=0xFF0080)
      embed.set_image(url = ctx.author.avatar_url)
      await ctx.send(embed=embed)
      return
    userAvatarUrl = member.avatar_url
    embed = discord.Embed(description = f'**Запросил: {ctx.author.name}**', icon_url=ctx.author.avatar_url,color=0xFF0080)
    embed.add_field(name=" Аватар:", value=member.mention, inline=False)
    embed.set_image(url = member.avatar_url)
    await ctx.send(embed=embed)


  
@client.command(name="аватар")
async def avatar(ctx, *, member : discord.Member=None):
    if member == None:
      embed = discord.Embed(description = f'**Запросил: {ctx.author.name}**', icon_url=ctx.author.avatar_url,color=0xFF0080)
      embed.set_image(url = ctx.author.avatar_url)
      await ctx.send(embed=embed)
      return
    userAvatarUrl = member.avatar_url
    await ctx.message.delete()
    embed = discord.Embed(description = f'**Запросил: {ctx.author.name}**', icon_url=ctx.author.avatar_url,color=0xFF0080)
    embed.add_field(name=" Аватар:", value=member.mention, inline=False)
    embed.set_image(url = member.avatar_url)
    await ctx.send(embed=embed)





guild_ids = [831071829170061326]


@slash.slash(name="Поцеловать",
             description="Поцеловать человека.",
             options=[
               create_option(
                 name="member",
                 description="Да, поцеловать",
                 option_type=6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=True
               )
             ])
async def поцеловать(ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://images-ext-1.discordapp.net/external/LbvbptPGA0pEm7S5qMgWsyX1TFg_V3F4lvdWG8XUj1I/https/i.imgur.com/Ui0Gy9z.gif",
            "https://images-ext-1.discordapp.net/external/q0qLf9Qtjnp5McTDAojwv6wL9Xyi7KXajA82YfUtmWY/https/i.imgur.com/fSCM7Wu.gif",
            "https://images-ext-2.discordapp.net/external/8W78jkO-sBo2s23sZeXMPrzJRLXjeTbMLPIkPX-8Bzw/https/i.imgur.com/x2gEP9W.gif",
            "https://images-ext-1.discordapp.net/external/E-bP2MnAHfdIexUV79D1DMgxc6O72g3zxoEpcDFHH7U/https/i.imgur.com/pKwOitS.gif",
            "https://c.tenor.com/Daj-Pn82PagAAAAM/gif-kiss.gif"
        ]
        if member == None:
            await ctx.send(embed = discord.Embed(description = '@Укажите участника', color=0xFF0080))
            return

        embed=discord.Embed(color = random.choice(colors))
        embed.set_author(name=f"{ctx.author} Поцеловал пользователя {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)

@slash.slash(name="Обнять",
             description="🥺 Обнять человека.",
             options=[
               create_option(
                 name="member",
                 description="Да, обнять",
                 option_type=6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=True
               )
             ])
async def obnat2(ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

        if member == None:
            await ctx.send(embed = discord.Embed(description = '@Укажите участника', color=0xFF0080))
            return

        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        em=discord.Embed(color = random.choice(colors))
        em.set_author(name=f"{ctx.author} Обнял пользователя {member}",icon_url=member.avatar_url)
        em.set_image(url=res['url'])
        em.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        em.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=em)







@client.command()
async def трахнуть(ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://c.tenor.com/4RIbgFCLRrUAAAAd/rikka-takanashi-bad-girl.gif",
            "https://c.tenor.com/XofRuAsQH7EAAAAC/anime-sexy.gif",
            "https://c.tenor.com/pdBIge5Z3WAAAAAd/miyuki-shiba-shy.gif"
        ]
        if member == None:
            await ctx.send(embed = discord.Embed(description = '@Укажите участника', color=0xFF0080))
            return
        await ctx.message.delete()
        embed=discord.Embed(color = random.choice(colors))
        embed.set_author(name=f"{ctx.author} Трахнул пользователя {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)



@slash.slash(name="Танцевать",
             description="Танцевать.",
             guild_ids=guild_ids,
             options=[
               create_option(
                 name="member",
                 description="Да, танцевать",
                 option_type=6,
                 required=True,
                 )
             ])
async def танцевать(ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://c.tenor.com/zlhLMAQCZZsAAAAM/dance-vr.gif",
            "https://c.tenor.com/P7QN5kqyiSQAAAAd/aharen-san-aharen-san-anime.gif",
            "https://c.tenor.com/AD70bmXloTcAAAAM/chika-dance-chika-chika-chika.gif",
            "https://c.tenor.com/gZ9NqWUT7x8AAAAC/anime-tv-show.gif"
        ]
        randomgifs2 = [
            "https://images-ext-1.discordapp.net/external/ZZ-Xu7DH76Mb76_HxgwMQ80FNwwsFD9RR8APaKzvjVs/https/i.imgur.com/NL0apZh.gif",
            "https://c.tenor.com/2vRn7mgoMRMAAAAM/cute-anime-dance.gif",
            "https://c.tenor.com/AD70bmXloTcAAAAM/chika-dance-chika-chika-chika.gif",
            "https://c.tenor.com/z85ySqaD6s0AAAAd/hayasaki.gif"
        ]
        if member == None:
         embed=discord.Embed(color = random.choice(colors))
         embed.set_author(name=f"Опа, смотрите как танцует: {ctx.author}",icon_url=ctx.author.avatar_url)
         randomgifs2 = random.choice(randomgifs2)
         embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
         embed.set_image(url = randomgifs2)
         embed.timestamp = datetime.datetime.utcnow()
         await ctx.send(embed = embed)
         return

        embed=discord.Embed(color = random.choice(colors))
        embed.set_author(name=f"Опа, смотрите как танцует: {ctx.author} с {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)

@slash.slash(name="Наказать",
             description="Наказать человека.",
             guild_ids=guild_ids,
             options=[
               create_option(
                 name="member",
                 description="Да, наказать",
                 option_type=6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=True
               )
             ])
async def наказать(ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://c.tenor.com/gScnebhgJn4AAAAC/taritari-anime-spank.gif",
            "https://c.tenor.com/LMKZH2bDKHsAAAAC/spank-anime.gif",
            "https://c.tenor.com/Dcdf0if-PlsAAAAC/anime-school-girl.gif",
            "https://c.tenor.com/PeJyQRCSHHkAAAAC/saki-saki-mukai-naoya.gif",
            "https://c.tenor.com/GBShVmDnx9kAAAAC/anime-slap.gif"
        ]
        if member == None:
            await ctx.send(embed = discord.Embed(description = '@Укажите участника', color=0xFF0080))
            return

        embed=discord.Embed(color = random.choice(colors))
        embed.set_author(name=f"{ctx.author} Наказал пользователя {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)

@slash.slash(name="трахнуть",
             description="😏 Трахнуть человека.",
             options=[
               create_option(
                 name="member",
                 description="Да, трахнуть",
                 option_type=6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=True
               )
             ])
async def trax(ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://c.tenor.com/4RIbgFCLRrUAAAAd/rikka-takanashi-bad-girl.gif",
            "https://c.tenor.com/XofRuAsQH7EAAAAC/anime-sexy.gif",
            "https://c.tenor.com/pdBIge5Z3WAAAAAd/miyuki-shiba-shy.gif"
        ]
        if member == None:
            await ctx.send(embed = discord.Embed(description = '@Укажите участника', color=0xFF0080))
            return

        embed=discord.Embed(color = random.choice(colors))
        embed.set_author(name=f"{ctx.author} Трахнул пользователя {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)







@slash.slash(name="погрустить",
             description="😭 Погрустить",
             options=[
             ])
async def grys(ctx):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://c.tenor.com/ZgbfJDDS9yQAAAAC/anime-depressed.gif",
            "https://c.tenor.com/PZlhV5eKTiMAAAAC/good-night.gif",
            "https://c.tenor.com/lIlIyhYkQk0AAAAC/homicide-detective.gif",
            "https://c.tenor.com/T1QjLw5bPFAAAAAC/depressed-sad.gif",
            "https://c.tenor.com/i3uWiBCMgh8AAAAC/sad-aesthetic.gif",
            "https://c.tenor.com/nhh1RwGnkbQAAAAC/sad-anime.gif"
        ]

        embed=discord.Embed(color = random.choice(colors))
        embed.set_author(name=f"{ctx.author} Грустит",icon_url=ctx.author.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed = embed)








  
# ----------------------------------- clear ---------------------------------- #
@client.command(name = "clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="", description=f"Удалил `{amount}` Сообщений!")    
    embed.set_author(name=f"Запросил: {ctx.author.name}")
    embed.set_footer(text=f"Запросил: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    massage = await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member = None, amout: str = None, *, reason = None):
	emb_user = discord.Embed(title = '**Уведомление - ban**', color=0xFF0080)
	emb_user.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
	emb_user.add_field(name = '**Причина:**', value = reason, inline = False)
	emb_user.add_field(name = '**Длительность:**', value = amout, inline = False)
	emb_user.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)

	emb_user_stop = discord.Embed(title = '**Уведомление - Unban**', color=0xFF0080)
	emb_user_stop.add_field(name = '**Снял:**', value = ctx.author.mention, inline = False)
	emb_user_stop.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)
	mute_role = discord.utils.get(ctx.message.guild.roles, id = 913903061200683068)

	if member is None:
		emb = discord.Embed(title = '[ERROR] ban', description = f'{ctx.author.mention}, Укажите пользователя!', color=0xFF0080)
		emb.add_field(name = 'Пример:', value = f'{ctx.prefix}ban[@участник] <время(с, м, ч, д)> [причина]', inline = False)
		emb.add_field(name = 'Пример 1:', value = f'{ctx.prefix}ban @soso4ka 1ч пример')
		emb.add_field(name = 'Время:', value = f'с - секунды\nм - минуты\nч - часы\nд - дни')

		await ctx.send(embed = emb)
	else:
		end_time = amout[-1:]
		time = int(amout[:-1])
		if time <= 0:
			emb = discord.Embed(title = '[ERROR]ban', description = f'{ctx.author.mention}, Время не может быть меньше 1!', color=0xFF0080)
			emb.add_field(name = 'Пример:', value = f'{ctx.prefix}ban [@участник] <время> [причина]', inline = False)
			emb.add_field(name = 'Пример 1:', value = f'{ctx.prefix}ban @Xpeawey 1ч пример')
			emb.add_field(name = 'Время:', value = f'с - секунды\nм - минуты\nч - часы\nд - дни')

			await ctx.send(embed = emb)
		else:
			if end_time == 'с':
				if reason is None:
					emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
					emb.add_field(name = 'Длительность:', value = '{} секунд'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
				else:
					emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = reason, inline = False)
					emb.add_field(name = 'Длительность:', value = '{} секунд'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
			elif end_time == 'м':
				if reason is None:
					emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
					emb.add_field(name = 'Длительность:', value = '{} минут'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
				else:
					emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = reason, inline = False)
					emb.add_field(name = 'Длительность:', value = '{} минут'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
			elif end_time == 'ч':
				if reason is None:
						emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
						emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
						emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
						emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
						emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
						emb.add_field(name = 'Длительность:', value = '{} ч'.format(time))
						await member.add_roles(mute_role)
						await ctx.send(embed = emb)
						await member.send(embed = emb_user)
						await asyncio.sleep(time *60 *60)
						await member.remove_roles(mute_role)
						await member.send(embed = emb_user_stop)
						emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
						emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
						emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
						emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
						emb.add_field(name = '**Причина:**', value = 'Не указано', inline = False)
						emb.add_field(name = '**Длительность:**', value = '{} ч'.format(time))
						await member.add_roles(mute_role)
						await ctx.send(embed = emb)
						await member.send(embed = emb_user)
						await asyncio.sleep(time *60 *60)
						await member.remove_roles(mute_role)
						await member.send(embed = emb_user_stop)
						emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
						emb.add_field(name = '**Выдал:', value = ctx.author.mention, inline = False)
						emb.add_field(name = '**Нарушитель:', value = member.mention, inline = False)
						emb.add_field(name = '**ID нарушителя:', value = member.id, inline = False)
						emb.add_field(name = '**Причина:', value = 'Не указано', inline = False)
						emb.add_field(name = '**Длительность:', value = '{} ч'.format(time))
						await member.add_roles(mute_role)
						await ctx.send(embed = emb)
						await member.send(embed = emb_user)
						await asyncio.sleep(time *60 *60)
						await member.remove_roles(mute_role)
						await member.send(embed = emb_user_stop)
				else:
					if time == '1':
						emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
						emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
						emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
						emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
						emb.add_field(name = '**Причина:**', value = reason, inline = False)
						emb.add_field(name = '**Длительность:**', value = '{} ч'.format(time))
						await member.add_roles(mute_role)
						await ctx.send(embed = emb)
						await member.send(embed = emb_user)
						await asyncio.sleep(time *60 *60)
						await member.remove_roles(mute_role)
						await member.send(embed = emb_user_stop)
					elif time == '4' or time == '3' or time == '2':
						emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
						emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
						emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
						emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
						emb.add_field(name = '**Причина:**', value = reason, inline = False)
						emb.add_field(name = '**Длительность:**', value = '{} ч'.format(time))
						await member.add_roles(mute_role)
						await ctx.send(embed = emb)
						await member.send(embed = emb_user)
						await asyncio.sleep(time *60 *60)
						await member.remove_roles(mute_role)
						await member.send(embed = emb_user_stop)
					elif time >= '5':
						emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
						emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
						emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
						emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
						emb.add_field(name = '**Причина:**', value = reason, inline = False)
						emb.add_field(name = '**Длительность:**', value = '{} ч'.format(time))

						await member.add_roles(mute_role)
						await ctx.send(embed = emb)
						await member.send(embed = emb_user)
						await asyncio.sleep(time *60 *60)
						await member.remove_roles(mute_role)
						await member.send(embed = emb_user_stop)
			elif end_time == 'д':
				if reason is None:
					emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
					emb.add_field(name = 'Длительность:', value = '{} день (ей)'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
				else:
					emb = discord.Embed(title = f'**System - ban**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = reason, inline = False)
					emb.add_field(name = 'Длительность:', value = '{} день (ей)'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60 *60 *24)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)

@client.command()
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member = None, amout: str = None, *, reason = None):
	emb_user = discord.Embed(title = '**Уведомление - mute**', color=0xFF0080)
	emb_user.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
	emb_user.add_field(name = '**Причина:**', value = reason, inline = False)
	emb_user.add_field(name = '**Длительность:**', value = amout, inline = False)
	emb_user.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)

	emb_user_stop = discord.Embed(title = '**Уведомление - Unmute**', color=0xFF0080)
	emb_user_stop.add_field(name = '**Снял:**', value = ctx.author.mention, inline = False)
	emb_user_stop.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)
	mute_role = discord.utils.get(ctx.message.guild.roles, id = 860588414227578921)

	if member is None:
		emb = discord.Embed(title = '[ERROR] mute', description = f'{ctx.author.mention}, Укажите пользователя!', color=0xFF0080)
		emb.add_field(name = 'Пример:', value = f'{ctx.prefix}mute[@участник] <время(с, м, ч, д)> [причина]', inline = False)
		emb.add_field(name = 'Пример 1:', value = f'{ctx.prefix}mute @soso4ka 1ч пример')
		emb.add_field(name = 'Время:', value = f'с - секунды\nм - минуты\nч - часы\nд - дни')

		await ctx.send(embed = emb)
	else:
		end_time = amout[-1:]
		time = int(amout[:-1])
		if time <= 0:
			emb = discord.Embed(title = '[ERROR]mute', description = f'{ctx.author.mention}, Время не может быть меньше 1!', color=0xFF0080)
			emb.add_field(name = 'Пример:', value = f'{ctx.prefix}mute [@участник] <время> [причина]', inline = False)
			emb.add_field(name = 'Пример 1:', value = f'{ctx.prefix}mute @soso4ka 1ч пример')
			emb.add_field(name = 'Время:', value = f'с - секунды\nм - минуты\nч - часы\nд - дни')

			await ctx.send(embed = emb)
		else:
			if end_time == 'с':
				if reason is None:
					emb = discord.Embed(title = f'**System - mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
					emb.add_field(name = 'Длительность:', value = '{} секунд'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
				else:
					emb = discord.Embed(title = f'**System - mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = reason, inline = False)
					emb.add_field(name = 'Длительность:', value = '{} секунд'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
			elif end_time == 'м':
				if reason is None:
					emb = discord.Embed(title = f'**System - mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
					emb.add_field(name = 'Длительность:', value = '{} минут'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
				else:
					emb = discord.Embed(title = f'**System -mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = reason, inline = False)
					emb.add_field(name = 'Длительность:', value = '{} минут'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
			elif end_time == 'ч':
				if reason is None:
					emb = discord.Embed(title = f'**System - mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
					emb.add_field(name = 'Длительность:', value = '{} h'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
				else:
					emb = discord.Embed(title = f'**System -mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = reason, inline = False)
					emb.add_field(name = 'Длительность:', value = '{} h'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
			elif end_time == 'д':
				if reason is None:
					emb = discord.Embed(title = f'**System - mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
					emb.add_field(name = 'Длительность:', value = '{} день (ей)'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60 *60 *24)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)
				else:
					emb = discord.Embed(title = f'**System - mute**', color=0xFF0080)
					emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
					emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
					emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
					emb.add_field(name = 'Причина:', value = reason, inline = False)
					emb.add_field(name = 'Длительность:', value = '{} день (ей)'.format(time))
					await member.add_roles(mute_role)
					await ctx.send(embed = emb)
					await member.send(embed = emb_user)
					await asyncio.sleep(time *60 *60 *24)
					await member.remove_roles(mute_role)
					await member.send(embed = emb_user_stop)




@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        if after.channel.id == 936641496919183390:
            category = after.channel.category
            
            channel2 = await member.guild.create_voice_channel(
                name     = f' || { member.display_name } Канал', 
                category = category
            )
            
            await channel2.set_permissions(member, connect = True, manage_channels = True, administrator = True, manage_permissions = True, )
            await member.move_to(channel2)

            def check(x, y, z): return len(channel2.members) == 0
            
            await client.wait_for('voice_state_update', check = check)
            await channel2.delete()

@client.event
async def on_message_delete(message):
    if message.author.bot:
        return

    if not message.attachments:
        log = client.get_channel(913524501617209364)
        #если участник удалил сообщение другого участника писать об этом
        e = discord.Embed(title=f'{message.author.display_name} удалил сообщение', timestamp = message.created_at, color=0xff0000)
        e.add_field(name='Сообщение:', value=f'{message.content}', inline=False)
        e.add_field(name='Канал:', value=f'{message.channel.mention}', inline=False)
        e.add_field(name='Участник:', value=f'{message.author.mention}', inline=False)
        e.set_thumbnail(url=message.author.avatar_url)
        return await log.send(embed=e)

    files = []
    for file in message.attachments:
        fp = io.BytesIO()
        await file.save(fp = f'log.jpg')

    log = client.get_channel(913524501617209364)
    e = discord.Embed(title=f'{message.author.display_name} удалил сообщение:',color=0xff0000)
    e.add_field(name='Канал:', value=f'{message.channel.mention}', inline=False)
    e.add_field(name='Участник:', value=f'{message.author.mention}', inline=False)
    e.set_thumbnail(url=message.author.avatar_url)
    file = discord.File(f"log.jpg",filename=f"log.jpg")
    e.set_image(url=f"attachment://log.jpg")
    await log.send(file=file,embed=e)
    
    







@client.event
async def on_guild_channel_create(channel):
    embed = discord.Embed(title=f"Создан новый канал!", color=0xff0000)
    embed.add_field(name='Имя канала:', value=f"`{channel.name}`", inline = False)
    embed.add_field(name='Категория канала:', value=channel.category, inline = False)
    embed.add_field(name='id канала:', value=channel.id, inline = False)
    embed.add_field(name='Дата создания:', value=channel.created_at, inline = False)
    channel = client.get_channel(913524501617209364)
    await channel.send(embed=embed)






@client.event
async def on_member_update(before, after):
    z = client.get_channel(913524501617209364)
    if len(before.roles) > len(after.roles):
        role = next(role for role in before.roles if role not in after.roles)
        embed = discord.Embed(title = f"{before} Роль была удалена", description = f"роль {role.name} удалена у  {before.mention}.", color = discord.Colour.red())
        
    elif len(after.roles) > len(before.roles):
        role = next(role for role in after.roles if role not in before.roles)
        embed = discord.Embed(title = f"{before} Получил новую роль", description = f"Роль {role.name} добавлена у  {before.mention}.", color = discord.Colour.green())
        
    elif before.nick != after.nick:
        embed = discord.Embed(title = f"{before} Ник изменен", description = f"До: **{before.nick}**\nПосле: **{after.nick}**", color = discord.Colour.blue())
    else:
        return
    async for event in before.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):
     embed.set_thumbnail(url=before.avatar_url)
     embed.timestamp = datetime.datetime.utcnow()
     await z.send(embed = embed)

@client.command(aliases=['кнб'])
async def rps(ctx, user_choice = None):
    if not user_choice:
        embed = discord.Embed(title="Ошибка :angry: ", description = f'{ctx.message.author.mention} укажите `камень`, `ножницы` или `бумага`!', timestamp = ctx.message.created_at, color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed)
        await ctx.message.delete()
        return
    rpsGame = ['камень', 'бумага', 'ножницы']
    if user_choice.lower() in rpsGame:
        bot_choice = random.choice(rpsGame)
        user_choice = user_choice.lower()
        if user_choice == bot_choice:
            embed = discord.Embed(title = 'Камень-Ножницы-Бумага', description=f'`{user_choice}`, говоришь? Посмотрим... А у нас тут `{bot_choice}`. У вас ничья!', color=0xFF0080)
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if user_choice == 'камень' and bot_choice == 'бумага':
            embed = discord.Embed(title = 'Камень-Ножницы-Бумага', description=f'`{user_choice}`, говоришь? Посмотрим... А у нас тут `{bot_choice}`. Вы проиграли!', color=0xFF0080)
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if user_choice == 'камень' and bot_choice == 'ножницы':
            embed = discord.Embed(title = 'Камень-Ножницы-Бумага', description=f'`{user_choice}`, говоришь? Посмотрим... А у нас тут `{bot_choice}`. Вы выйграли!', color=0xFF0080)
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if user_choice == 'бумага' and bot_choice == 'камень':
            embed = discord.Embed(title = 'Камень-Ножницы-Бумага', description=f'`{user_choice}`, говоришь? Посмотрим... А у нас тут `{bot_choice}`. Вы выйграли!', color=0xFF0080)
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if user_choice == 'бумага' and bot_choice == 'ножницы':
            embed = discord.Embed(title = 'Камень-Ножницы-Бумага', description=f'`{user_choice}`, говоришь? Посмотрим... А у нас тут `{bot_choice}`. Вы проиграли!', color=0xFF0080)
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if user_choice == 'ножницы' and bot_choice == 'бумага':
            embed = discord.Embed(title = 'Камень-Ножницы-Бумага', description=f'`{user_choice}`, говоришь? Посмотрим... А у нас тут `{bot_choice}`. Вы выйграли!', color=0xFF0080)
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if user_choice == 'ножницы' and bot_choice == 'камень':
            embed = discord.Embed(title = 'Камень-Ножницы-Бумага', description=f'`{user_choice}`, говоришь? Посмотрим... А у нас тут `{bot_choice}`. Вы проиграли!', color=0xFF0080)
            embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            await ctx.send(embed=embed)
            await ctx.message.delete()
    else:
        embed = discord.Embed(title="Ошибка :angry:", description = f'{ctx.message.author.mention} укажите `камень`, `ножницы` или `бумага`!', timestamp = ctx.message.created_at)
        embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed)
        await ctx.message.delete()

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   emb = discord.Embed(title="System - unmute", description=f" Мут снят-{member.mention}", color=0xFF0080)
   emb.add_field(name=f'Мут снял:', value=f'{ctx.author.mention}', inline=False)
   emb.add_field(name=f'Сервер:', value=f'{ctx.guild.name}', inline=False)
   await member.remove_roles(mutedRole)
   await member.send(embed=emb)
   embed = discord.Embed(title="System - unmute", description=f" Мут снят-{member.mention}", color=0xFF0080)
   embed.add_field(name=f'Мут снял:', value=f'{ctx.author.mention}', inline=False)
   embed.add_field(name=f'Сервер:', value=f'{ctx.guild.name}', inline=False)
   await ctx.send(embed=embed)
   await ctx.message.delete()
   


@client.command(name="инфасервер")
async def serverinfo(ctx):

    text_channel_server = len(ctx.message.guild.channels)
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
        
    embed2 = discord.Embed(timestamp=ctx.message.created_at, color=0xFF0080)
    embed2.add_field(name='Название сервера', value=f"{ctx.guild.name}", inline=False)
    embed2.add_field(name='Создатель сервера', value="<@!403875492496670732>", inline=False)
    embed2.add_field(name='Уровень верификации', value="medium", inline=False)
    embed2.add_field(name='Высшая роль', value=ctx.guild.roles[-1], inline=False)

    for r in staff_roles:
        role = discord.utils.get(ctx.guild.roles, name=r)
        if role:
            members = '\n'.join([member.name for member in role.members]) or "None"
            embed2.add_field(name=role.name, value=members)

    embed2.add_field(name='✅Количество ролей', value=str(role_count), inline=False)
    embed2.add_field(name="🚶Количество участников ", value=ctx.guild.member_count, inline=False)
    embed2.add_field(name="💬Текстовые каналы:", value=len(ctx.message.guild.channels), inline=False)
    embed2.add_field(name="🔊Голосовые каналы:", value=len(ctx.message.guild.voice_channels), inline=True)
    embed2.set_thumbnail(url=ctx.guild.icon_url)
    embed2.add_field(name="🚀Бустов:", value=f'{str(ctx.guild.premium_subscription_count)}', inline=False)
    embed2.add_field(name='Создан:', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    
    await ctx.message.delete()
    await ctx.send(embed=embed2)


@client.command(aliases = ['userinfo', 'uinfo', 'юзер', 'инфо'])
async def user(ctx,member:discord.Member = None):

    if member==None:
        member=ctx.author

    rlist = []
    for role in member.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    py_dt = member.joined_at
    epoch = round(py_dt.timestamp())

    py_dt1 = member.created_at
    epoch1 = round(py_dt1.timestamp())
  
    b = ", ".join(rlist)
    date_format = "%a, %b %d, %Y @ %I:%M %p" 
    if member == None:
        member = ctx.author
    if member.nick == None:
        nick = member.name
    else:
        nick = member.nick
    emb = discord.Embed(title = f'**Информация о {member.name}**',description = f'''
Никнейм на сервере: {nick}
Айди: {member.id}

**Аватар:** [[клик]({member.avatar_url})]
**Тег:** {member.discriminator}
**Всего ролей:** {len(rlist)}
{''.join([b])}
**Гл.Роль:** {member.top_role.mention}
    
**Дата создания аккаунта:** <t:{epoch1}:D> <t:{epoch1}:R>
**Дата входа на сервер:** <t:{epoch}:D> <t:{epoch}:R>
                        ''', timestamp=ctx.message.created_at,color=0xFF0080 )
    emb.set_footer(text=f'Запросил - {ctx.author}',
  icon_url=ctx.author.avatar_url,)
    emb.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed = emb)
    await ctx.message.delete()

@slash.slash(name="инфа",
             description="Информация о пользователе",
             guild_ids=guild_ids,
             options=[
               create_option(
                 name="member",
                 description="Да, инфа и что",
                 option_type=6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=True
               )
             ])
async def user(ctx,member:discord.Member = None):

    if member==None:
        member=ctx.author

    rlist = []
    for role in member.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)


    datetime.datetime(2013, 10, 4, 23, 27, 14, 678151)
    py_dt = member.joined_at
    epoch = round(py_dt.timestamp())

    py_dt1 = member.created_at
    epoch1 = round(py_dt1.timestamp())
  
    b = ", ".join(rlist)
    date_format = "%a, %b %d, %Y @ %I:%M %p" 
    if member == None:
        member = ctx.author
    if member.nick == None:
        nick = member.name
    else:
        nick = member.nick
    emb = discord.Embed(title = f'**Информация о {member.name}**',description = f'''
Никнейм на сервере: {nick}
Айди: {member.id}

**Аватар:** [[клик]({member.avatar_url})]
**Тег:** {member.discriminator}
**Всего ролей:** {len(rlist)}
{''.join([b])}
**Гл.Роль:** {member.top_role.mention}
    
**Дата создания аккаунта:** <t:{epoch1}:D> <t:{epoch1}:R>
**Дата входа на сервер:** <t:{epoch}:D> <t:{epoch}:R>
                        ''',color=0xFF0080 )
    emb.set_footer(text=f'Запросил - {ctx.author}',
  icon_url=ctx.author.avatar_url,)
    emb.timestamp = datetime.datetime.utcnow()
    emb.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed = emb)










player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(name = "крестики")
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if ctx.channel.id != 965699411499966474:
        embed = discord.Embed(title="Крестики нолики", description="Используйте команду в <#965699411499966474>", color=0x00ff00)
        await ctx.send(embed = embed)
        return

  
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            embed = discord.Embed(title="Крестики нолики", description="Твой ход: <@" + str(player1.id) + "> (чтобы ходить, -ходить 1-9)", color=0x00ff00)
            await ctx.send(embed = embed)
        elif num == 2:
            turn = player2
            embed = discord.Embed(title="Крестики нолики", description="Твой ход: <@" + str(player2.id) + "> (чтобы ходить, -ходить 1-9)", color=0x00ff00)
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="Крестики нолики", description="Игра уже идет!  Закончите её, прежде чем начинать новую.", color=0x00ff00)
        await ctx.send(embed = embed)

@client.command(name="ходить")
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if ctx.channel.id != 965699411499966474:
        embed = discord.Embed(title="Крестики нолики", description="Используйте команду в <#965699411499966474>", color=0x00ff00)
        await ctx.send(embed = embed)
        return
  
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    embed = discord.Embed(title="Крестики нолики", description=mark + " Выиграл!", color=0x00ff00)
                    await ctx.send(embed = embed)
                elif count >= 9:
                    gameOver = True
                    embed = discord.Embed(title="Крестики нолики", description="Ничья!", color=0x00ff00)
                    await ctx.send(embed = embed)
                    await ctx.message.delete()

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                embed = discord.Embed(title="Крестики нолики", description="Обязательно выберите целое число от 1 до 9 (включительно) и неотмеченную плитку.", color=0x00ff00)
                await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title="Крестики нолики", description="Это не твоя очередь.", color=0x00ff00)
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title="Крестики нолики", description="Пожалуйста, начните новую игру, используя команду -крестики", color=0x00ff00)
        await ctx.send(embed = embed)
        await ctx.message.delete()



def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Крестики нолики", description="Пожалуйста, укажите 2 игроков для этой команды. Пример: -крестики <@414345181979213826> <@303173015380951044>", color=0x00ff00)
        await ctx.send(embed = embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="Крестики нолики", description="Пожалуйста, не забудьте упомянуть/пинговать игроков (например, <@303173015380951044>).", color=0x00ff00)
        await ctx.send(embed = embed)


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Крестики нолики", description="Пожалуйста, введите позицию, которую вы хотите отметить.", color=0x00ff00)
        await ctx.send(embed = embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="Крестики нолики", description="Пожалуйста, не забудьте ввести целое число.", color=0x00ff00)
        await ctx.send(embed = embed)

#стоп команда для остановки игры
@client.command(name="стоп")
async def stop(ctx):
    global gameOver
    gameOver = True
    embed = discord.Embed(title="Игра закончена", description="Игра закончена пользователем <@" + str(ctx.author.id) + ">", color=0x00ff00)
    await ctx.send(embed=embed)
    await ctx.message.delete()









@client.group(invoke_without_command = True)
async def help(ctx):
    embed=discord.Embed(title="Вы можете получить подробную справочную информацию для каждой команды, вызвав ее с помощью - Например: -help music покажет вам информацию о каждой команте music", color=0xff00ff)
    embed.set_author(name="Основные команды:")
    embed.add_field(name="<:music:975749622125432873>  Music (-help music) :", value="`+play`  `+stop`  `+pause` ` +resume`  `+queue`  `+skip`  `+remove` `+disconnect` `+repeat`", inline=False)
    embed.add_field(name="<:drama:975750287107178506>  Fun (-help fun)", value="`-обнять @` `-трахнуть @`  `-наказать @` `-поцеловать @` `-крестики @ @`  `-грусть` ``-инфа`` ``-инфасервер`` ``-кнб`` ``-аватар @``", inline=False)
    embed.add_field(name="<:crown22:975750848711905322>  Moderation (-help moderation)", value="`-clear ` `-ban ` `-mute ` `-unmute `", inline=False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/713134078647337060/975756403937513573/Screenshot_2.png")
    embed.set_footer(text="𝐠 𝐨 𝐝 ' 𝐬 🎄 © 2022",icon_url="https://cdn.discordapp.com/avatars/938058016438239282/d5d96553594e04b7f47e85cbffda11f8.png?size=4096")
    await ctx.message.delete()
    msg = await ctx.send(embed=embed,
    components=[
            SelectMenu(
                        options=[
                            SelectOption(
                                label="Help Music",
                                value="option1",
                                description="Информация о музыке",
                                emoji="🎵" # you can use discord.Parti ... emoji to use a custom one (i dont know what its called)
                            ),
                            SelectOption(
                                label="Help Fun",
                                value="option2",
                                description="Информация о раздоре",
                                emoji="😄" # you can use discord.Parti ... emoji to use a custom one (i dont know what its called)
                            ),
                            SelectOption(
                                label="Help Moderation",
                                value="option3",
                                description="Информация о модерировании",
                                emoji="🛡️" # you can use discord.Parti ... emoji to use a custom one (i dont know what its called)
                            ),
                            SelectOption(
                                label="Назад",
                                value="option4",
                                description="Вернуться назад",
                                emoji="🛑" # you can use discord.Parti ... emoji to use a custom one (i dont know what its called)
                            ),

                        ])]
                        ) 

@client.event
async def on_select_option(interaction):
    await interaction.respond(type=6)
    if interaction.values[0] == "option2":
        e1 = discord.Embed(title="   Мьзик команды",color=0xFF0080 ,description="""
   
      ```             play``` Воспроизвести музыку.
      ```             stop``` Остановить музыку.
      ```             pause``` Поставить музыку на паузу.
      ```             resume``` Продолжить музыку.               
      ```             skip``` Пропустить трэк.
      ```             queue``` Посмотреть очередь трэков.
      ```             Join``` Бот присоедениться к вам в гс.
      ```             repeat``` Повторить музыку 2 раза.
      ```             remove``` Удалить музыку из очереди
      +remove номер музыки в очереди (+queue).
      ```             disconnect``` Очистить очередь музыки
      и удалить бота из гс
    """)
        await interaction.send(embed=e1)
    elif interaction.values[0] == "option3":
        e3 = discord.Embed(title="Модератор команды",color=0xFF0080 , description="""
    ```             clear``` Очистить чат от сообещний +clear число"
    ```             ban``` Забанить человека -ban @ (время 1с, 1м, 1ч, 1д) (причина)
    ```             mute``` Замьютить человека -mute @ (время 1с, 1м, 1ч, 1д) (причина)
    ```             unmute``` Размьютить человека -unmute @
    """)
        await interaction.send(embed=e3)
    elif interaction.values[0] == "option1":
        e2 = discord.Embed(title="Fun команды",color=0xFF0080 , description="""
      ```       обнять``` Обнять человека. @
      ```       Трахнуть``` Трахнуть человека. @
      ```       Наказать``` Наказать человека. @ 
      ```       Грусть``` Погрустить.
      ```       Поцеловать``` Поцеловать челока. @
      ```       аватар``` Показать аватарку человека. @
      ```       инфа```  Показать информацию о user. @
      ```       инфасервер``` Показать информацию о сервере.
      ```       8ball``` Шар судьбы, (!8ball вопрос)
      ```       кнб``` сыграть в камень ножницы бумага.
      ```       Крестики``` сыграть в крестики нолики (@упомянуть себя @упомянуть друга)
      """)
        await interaction.send(embed=e2)
    elif interaction.values[0] == "option4":
        embed=discord.Embed(title="Вы можете получить подробную справочную информацию для каждой команды, вызвав ее с помощью - Например: -help music покажет вам информацию о каждой команте music", color=0xff00ff)
        embed.set_author(name="Основные команды:")
        embed.add_field(name="🎵  Music (-help music) :", value="`+play`  `+stop`  `+pause` ` +resume`  `+queue`  `+skip`  `+remove` `+disconnect` `+repeat`", inline=False)
        embed.add_field(name="😄  Fun (-help fun)", value="`-обнять @` `-трахнуть @`  `-наказать @` `-поцеловать @` `-крестики @ @`  `-грусть` ``-инфа`` ``-инфасервер`` ``-кнб`` ``-аватар @``", inline=False)
        embed.add_field(name="🛡️  Moderation (-help moderation)", value="`-clear ` `-ban ` `-mute ` `-unmute `", inline=False)
        embed.set_thumbnail(url="https://images8.alphacoders.com/102/1026336.jpg")
        embed.set_footer(text="𝐠 𝐨 𝐝 ' 𝐬 🎄 © 2022",icon_url="https://cdn.discordapp.com/avatars/303173015380951044/2664eb6a0d92cf4eb18237f349b88051.webp?size=32")
        await interaction.send(embed=embed)


@help.command() 
async def music(ctx):
   embed = discord.Embed(title="   Мьзик команды",color=0xFF0080 ,description="""
   
      ```             play``` Воспроизвести музыку.
      ```             stop``` Остановить музыку.
      ```             pause``` Поставить музыку на паузу.
      ```             resume``` Продолжить музыку.               
      ```             skip``` Пропустить трэк.
      ```             queue``` Посмотреть очередь трэков.
      ```             Join``` Бот присоедениться к вам в гс.
      ```             repeat``` Повторить музыку 2 раза.
      ```             remove``` Удалить музыку из очереди
      +remove номер музыки в очереди (+queue).
      ```             disconnect``` Очистить очередь музыки
      и удалить бота из гс
    """)
   await ctx.send(embed=embed)
   await ctx.message.delete()

@help.command() 
async def fun(ctx):
    embed = discord.Embed(title="Fun команды",color=0xFF0080 , description="""
      ```       обнять``` Обнять человека. @
      ```       Трахнуть``` Трахнуть человека. @
      ```       Наказать``` Наказать человека. @ 
      ```       Грусть``` Погрустить.
      ```       Поцеловать``` Поцеловать челока. @
      ```       аватар``` Показать аватарку человека. @
      ```       инфа```  Показать информацию о user. @
      ```       инфасервер``` Показать информацию о сервере.
      ```       8ball``` Шар судьбы, (!8ball вопрос)
      ```       кнб``` сыграть в камень ножницы бумага.
      ```       Крестики``` сыграть в крестики нолики (@упомянуть себя @упомянуть друга)
      """)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@help.command() 
async def moderation(ctx):
    embed = discord.Embed(title="Модератор команды",color=0xFF0080 , description="""
    ```             clear``` Очистить чат от сообещний +clear число"
    ```             ban``` Забанить человека -ban @ (время 1с, 1м, 1ч, 1д) (причина)
    ```             mute``` Замьютить человека -mute @ (время 1с, 1м, 1ч, 1д) (причина)
    ```             unmute``` Размьютить человека -unmute @
    """)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
async def role(ctx):

    emb = discord.Embed(
        description = 
        f"""
        Чтобы изменить цвет своего ника, выберите одну из кнопок.
        
        """,
        color=0xFF0080
    )
    emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/937772492456607756/972582475731705886/1-removebg-preview.png')
    emb.set_author(name = 'Изменить цвет')
    emb.set_footer(text="Часто роли лучше не менять, а до дискорд жалуется",icon_url="https://cdn.discordapp.com/avatars/938058016438239282/d5d96553594e04b7f47e85cbffda11f8.webp?size=80")

    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = 'Розовый',
            custom_id = 'rosovi'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Зелёный',
            custom_id = 'green'
    ),
        Button(
            style = ButtonStyle.gray,
            label = 'Синий',
            custom_id = 'blue'
    ),
        Button(
            style = ButtonStyle.gray,
            label = 'Фиолетовый',
            custom_id = 'purple'
    )
    )
    await ctx.send("@here",embed = emb, components = [row])
    await ctx.message.delete()
    

@client.event
async def on_button_click(inter):

    res = 'Вы успешно поменяли цвет ника!' 
    res1 = 'Вы успешно поменяли цвет ника!' 
    res2 = 'Вы успешно поменяли цвет ника!' 
    res3 = 'Вы успешно поменяли цвет ника!' 
    guild = client.get_guild(inter.guild.id)

    if inter.component.id == "rosovi":
        verif = guild.get_role(972575263403696158)
        verif2 = guild.get_role(972576520226881597)
        verif3 = guild.get_role(972576572571811960)
        verif4 = guild.get_role(972576911102476328)
        member = inter.author
        await member.add_roles(verif)
        await member.remove_roles(verif2,verif3,verif4)
        await inter.send(res, ephemeral = True)
    elif inter.component.id == "green":
        verif = guild.get_role(972576520226881597)
        verif2 = guild.get_role(972575263403696158)
        verif3 = guild.get_role(972576572571811960)
        verif4 = guild.get_role(972576911102476328)
        member = inter.author
        await member.add_roles(verif)
        await member.remove_roles(verif4)
        await inter.send(res1, ephemeral = True)
    elif inter.component.id == "blue":
        verif = guild.get_role(972576572571811960)
        verif2 = guild.get_role(972575263403696158)
        verif3 = guild.get_role(972576520226881597)
        verif4 = guild.get_role(972576911102476328)
        member = inter.author
        await member.add_roles(verif)
        await member.remove_roles(verif2,verif3,verif4)
        await inter.send(res2, ephemeral = True)
    elif inter.component.id == "purple":
        verif = guild.get_role(972576911102476328)
        verif2 = guild.get_role(972575263403696158)
        verif3 = guild.get_role(972576572571811960)
        verif4 = guild.get_role(972576520226881597)
        member = inter.author
        await member.add_roles(verif)
        await member.remove_roles(verif2,verif3,verif4)
        await inter.send(res3, ephemeral = True)
        
@commands.cooldown(1, 3600, commands.BucketType.user)
@client.command()
async def find(ctx):
    #запретить человеку использовать команду по id
    if ctx.author.id == 513012277201338398:
        await ctx.send("Матика, ты дебил, хватит спамить этой командой, :клоун:")
        return
    msg = await ctx.send('Обнаружение гея началось...')
    random_number = random.randint(0, 10)
    random_number2 = random.randint(11, 35)
    random_number3 = random.randint(36, 45)
    random_number4 = random.randint(46, 70)
    random_number5 = random.randint(71, 85)
    random_number6 = random.randint(86, 99)
    await asyncio.sleep(3)
    await msg.edit(content=f"{random_number}%")
    #через время изменить сообщение
    await asyncio.sleep(3)
    await msg.edit(content=f"{random_number2}%")
    #через время изменить сообщение
    await asyncio.sleep(3)
    await msg.edit(content=f"{random_number3}%")
    #через время изменить сообщение
    await asyncio.sleep(3)
    await msg.edit(content=f"{random_number4}%")
    #через время изменить сообщение
    await asyncio.sleep(3)
    await msg.edit(content=f"{random_number5}%")
    #через время изменить сообщение
    await asyncio.sleep(3)
    await msg.edit(content=f"{random_number6}%")
    #через время изменить сообщение
    await asyncio.sleep(3)
    #редактировать сообщение
    await msg.edit(content="100%")
    await asyncio.sleep(1)
    member = random.choice(ctx.guild.members)
    #рандомные числа от 0 до 100
    emb = discord.Embed(title = f'Гей найден!',description = "{}".format(member.mention))
    #указать аватар человека который рандомно выбран
    emb.set_thumbnail(url=member.avatar_url)
    #указать время
    emb.set_footer(text=f'Запросил - {ctx.author}',
    icon_url=ctx.author.avatar_url,)
    await msg.edit(embed=emb)
        
@client.event
async def on_message_edit(before, after):
    z = client.get_channel(913524501617209364)
    if before.author.bot:
        return
    guild = before.guild
    embed = discord.Embed(title = f"{before.author} Отредактировал свое сообщение", description = f"До: **{before.content}**\nПосле: **{after.content}**\nАвтор: {before.author.mention}\nКанал: {before.channel.mention}", color = discord.Colour.blue())
    embed.timestamp = datetime.datetime.utcnow()
    await z.send(embed = embed)


    
@client.command()
@commands.has_permissions(administrator=True)
async def delrole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send("Роль удалена")



client.run("OTM4MDU4MDE2NDM4MjM5Mjgy.Gw-8uy.y2WAN-rIgzc8sxOQK6mgWVMNxOizVxs0k8yYD0")


