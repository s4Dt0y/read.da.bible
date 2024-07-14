"""cog that contains general stuff"""

from config import EXTENSIONS

from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='Check if the bot is responsive')
    async def ping(self, ctx):
        """is it up ??"""
        await ctx.send('Pong!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx):
        """reload all my extensions"""
        for ext in EXTENSIONS:
            await self.bot.reload_extension(ext)
        await ctx.send("Extensions reloaded")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sync(self, ctx):
        """sync the tree"""
        await self.bot.tree.sync()
        await ctx.send("Command tree synced")


async def setup(bot):
    """setup everything"""
    await bot.add_cog(General(bot))
