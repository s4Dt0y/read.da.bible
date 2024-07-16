import random
import traceback
import pythonbible as bible

import discord
from discord.ext import commands


class Play(commands.Cog):
    """Fun stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="verse", with_app_command=True)
    async def verse(self, ctx):
        """send a random verse"""

        with open("verses.dat", "r") as file:
            lines = file.readlines()
            random.shuffle(lines)
            verse = random.choice(lines).replace("\n", "")
        references = bible.get_references(verse)
        verse_id = bible.convert_reference_to_verse_ids(references[0])

        verse_text = bible.get_verse_text(verse_id[0], version=bible.Version.KING_JAMES)

        await ctx.send(verse_text)

    @verse.error
    async def verse_error(self, ctx, error):
        """handling errors for the verse command"""
        embed = discord.Embed(title="Error")
        print(type(error))

        if isinstance(error, commands.errors.CommandInvokeError):
            error = error.original

        if isinstance(error, IndexError):
            embed.description = "Command failed (faulty data file). Please try again."
        else:
            error_data = "".join(traceback.format_exception(type(error), error, error.__traceback__))
            embed.description = f"Unknown error\n```py\n{error_data[:1000]}\n```"

        await ctx.send(embed=embed)



async def setup(bot):
    """set up everything"""
    await bot.add_cog(Play(bot))
