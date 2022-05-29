import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import html2text
import TOKENFILE
import math
intents = discord.Intents.all()
client = commands.Bot(command_prefix='m!', intents=intents)

@client.command(name='usersonline')
async def usersonline(context):
    url = 'http://ntsfranz.crabdance.com/how_many_monke'
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content, 'lxml')
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text = text_maker.handle(soup.prettify())
    await context.message.channel.send(str(text))
@client.command(name='rgbtomonke')
async def rgbtomonke(context, r, g, b):
    m1raw = int(r) / 25.5
    m2raw = int(g) / 25.5
    m3raw = int(b )/ 25.5
    m1 = round(m1raw)
    m2 = round(m2raw)
    m3 = round(m3raw)
    await context.message.channel.send(str(m1) + " " + str(m2) + " " + str(m3))

client.run(TOKENFILE.TOKEN)