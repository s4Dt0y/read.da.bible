"""this is a bot"""

import discord
from discord.ext import commands

from utils.config import TOKEN, EXTENSIONS

class BibleBot(commands.Bot):
    async def setup_hook(self):
        """do stuff"""

        print(f"I am {self.user}")
        for ext in EXTENSIONS:
            await self.load_extension(ext)


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    bot = BibleBot(intents=intents, command_prefix=";")
    bot.run(str(TOKEN))
