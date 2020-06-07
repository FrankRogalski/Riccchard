import discord.message

classes = None
keyword = "help"
helping = f"|{keyword} [Command] - Tells you stuff about the commands"

def use(message: discord.message) -> str:
    msg = message.content.split()[1:]

    if msg:
        command = classes.get(msg[0])
        if command: return f"```{command.helping}```"
    
    out = "\n".join(command.helping for command in classes.values())
    return f"```{out}```"
