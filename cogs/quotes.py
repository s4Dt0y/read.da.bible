import requests
from fortune import fortune

import discord
from discord.ext import commands


class Quotes(commands.Cog):
    """commands that spout random quotes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="quotes", with_app_command=True)
    async def quotes(self, ctx, type=None):
        """send a random quote"""

        help_message = "Registered types: " + "help, random, chill"

        if type is None:
            await ctx.send(fortune())
        elif type == "random":
            await ctx.send(fortune())
        elif type == "chill":
            req = requests.get("https://zenquotes.io/api/random/")

            resp = req.json()[0]

            quote = resp["q"]
            author = resp["a"]

            mess = f"{quote} \n\\- {author}"

            await ctx.send(mess)
        elif type == "help":
            await ctx.send(help_message)
        else:
            await ctx.send(help_message)

async def setup(bot):
    """set up everything"""
    await bot.add_cog(Quotes(bot))
