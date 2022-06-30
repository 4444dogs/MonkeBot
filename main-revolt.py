import revolt
import asyncio
import aiohttp
from revolt.ext import commands
import requests
from bs4 import BeautifulSoup
import html2text
import TOKENFILE

class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "m!"
    @commands.command(name='usersonline')
    async def usersonline(self, ctx: commands.Context):
        url = 'http://ntsfranz.crabdance.com/how_many_monke'
        url_get = requests.get(url)
        soup = BeautifulSoup(url_get.content, 'lxml')
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        text = text_maker.handle(soup.prettify())
        await ctx.message.channel.send(str(text))
    @commands.command(name='rgbtomonke')
    async def rgbtomonke(self, ctx: commands.Context, r, g, b):
        m1raw = commands.IntConverter(r) / 25.5
        m2raw = commands.IntConverter(g) / 25.5
        m3raw = commands.IntConverter(b) / 25.5
        m1 = round(m1raw)
        m2 = round(m2raw)
        m3 = round(m3raw)
        await ctx.message.channel.send(str(m1) + " " + str(m2) + " " + str(m3))
    @commands.command(name='monketorgb')
    async def monketorgb(self, ctx: commands.Context, m1, m2, m3):
        Rraw = commands.IntConverter(m1) * 25.5
        Graw = commands.IntConverter(m2) * 25.5
        Braw = commands.IntConverter(m3) * 25.5
        R = round(Rraw)
        G = round(Graw)
        B = round(Braw)
        await ctx.message.channel.send(str(R) + " " + str(G) + " " + str(B))


async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, TOKENFILE.REVOLTTOKEN)
        await client.start()

asyncio.run(main())
