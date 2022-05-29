import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import html2text
import TOKENFILE
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

client.run(TOKENFILE.TOKEN)