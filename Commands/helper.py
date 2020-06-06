classes = None
keyword = "help"
helping = f"|{keyword} [Command] - Tells you stuff about the commands"

def use(msg):
    msg = msg.content.split(" ")

    if len(msg) > 1:
        command = classes.get(msg[1])
        if command: return f"```{command.helping}```", False
    
    out = "\n".join(command.helping for command in classes.values())
    return f"```{out}```", False
