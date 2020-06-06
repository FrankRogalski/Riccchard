import asyncio
import discord

from Commands.Convert import Convert
from Commands.Help import Help
from Commands.Flip import Flip
from Commands.Tuncer import Tuncer
from Commands.Hacki import Hacki
from Commands.Repeat import Repeat
from Commands.Say import Say
from Commands.Tunjaja import Tunjaja
from Commands.Spacey import Spacey
from Commands.Vote.VoteManagement import VoteManagement
from Commands.CanIHazDadJoke import CanIHazDadJoke

if __name__ == "__main__":
    commands = {i.get_keyword(): i for i in (Help(), Convert(), Flip(), Hacki(), Repeat(), Say(), Spacey(), Tuncer(), VoteManagement(), Tunjaja(), CanIHazDadJoke())}
    commands["help"].set_class_list(commands)

    client = discord.Client()
    
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        i = message.content.find(" ")
        command = commands.get(message.content[1:(i if i != -1 else len(message.content))])
        if command and message.content.startswith("|"):
            ans = command.use(message)
            await message.channel.send(ans[0], tts=ans[1])

    client.run('Mzk1NjMwOTk5ODAwNzc0NjY2.XtKGNA.ZhhIlxMP5vR_3P1tVAAPj7Rd26k')