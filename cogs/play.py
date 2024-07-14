import requests

import discord
from discord import app_commands
from discord.ext import commands

from fortune import fortune

class Play(commands.Cog):
    """Fun stuff"""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='quote')
    async def quote(self, interaction: discord.Interaction):
        """send a random quote"""
        await interaction.response.send_message(fortune())

    @app_commands.command(name='chill')
    async def chill(self, interaction: discord.Interaction):
        """send a random calling quote"""
        req = requests.get("https://zenquotes.io/api/random/")

        resp = req.json()[0]

        quote = resp['q']
        author = resp['a']

        mess = f'{quote} \n\\- {author}'

        await interaction.response.send_message(mess)

async def setup(bot):
    """set up everything"""
    await bot.add_cog(Play(bot))
