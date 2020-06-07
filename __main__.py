import asyncio
import discord
from typing import Union, Tuple

from commands import convert, countdown, dad, flip, hacki, helper, repeat, say, spacey, tuncer, tunjaja
import commands.vote.voteManagement as voteManagement
import config

async def send_message(message: discord.message, text: Union[str, Tuple[str, bool]]):
    if (type(text) == str):
        await message.channel.send(text)
    else:
        await message.channel.send(text[0], tts=text[1])

if __name__ == "__main__":
    commands = {i.keyword: i for i in (convert, countdown, dad, flip, hacki, helper, repeat, say, spacey, tuncer, tunjaja, voteManagement)}
    commands["help"].classes = commands

    client = discord.Client()
    
    @client.event
    async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print("------")

    @client.event
    async def on_message(message: discord.message):
        i = message.content.find(" ")
        command = commands.get(message.content[1:(i if i != -1 else None)])
        if command and message.content.startswith("|"):
            await send_message(message, command.use(message))
            

    client.run(config.token)