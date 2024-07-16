"""cog that contains general stuff"""

import discord
from discord.ext import commands

from utils.config import EXTENSIONS


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        """check if i am up"""
        await ctx.send("Pong!")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        """reload all my extensions"""
        for ext in EXTENSIONS:
            await self.bot.reload_extension(ext)
        await ctx.send("Extensions reloaded")

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        """sync my tree"""
        await self.bot.tree.sync()
        await ctx.send("Command tree synced")

    async def on_cog_command_error(self, ctx, error):
        """error handling"""
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions.")


async def setup(bot):
    """setup everything"""
    await bot.add_cog(General(bot))
