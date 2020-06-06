import asyncio
import discord

from commands import convert, countdown, dad, flip, hacki, helper, repeat, say, spacey, tuncer, tunjaja
import commands.vote.voteManagement as voteManagement
import config

if __name__ == "__main__":
    commands = {i.get_keyword(): i for i in (convert, countdown, dad, flip, hacki, helper, repeat, say, spacey, tuncer, tunjaja, voteManagement)}
    commands["help"].set_class_list(commands)

    client = discord.Client()
    
    @client.event
    async def on_ready():
        print("Logged in as")
        print(client.user.name)
        print(client.user.id)
        print("------")

    @client.event
    async def on_message(message):
        i = message.content.find(" ")
        command = commands.get(message.content[1:(i if i != -1 else len(message.content))])
        if command and message.content.startswith("|"):
            ans = command.use(message)
            await message.channel.send(ans[0], tts=ans[1])

    client.run(config.token)