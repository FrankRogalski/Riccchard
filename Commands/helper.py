classes = {}

def set_class_list(i_classes):
    global classes
    classes = i_classes

def use(msg):
    msg = msg.content.split(" ")

    if len(msg) > 1:
        command = classes.get(msg[1])
        if command: return f"```{command.helping()}```", False
    
    out = "\n".join(command.helping() for command in classes.values())
    return f"```{out}```", False

def get_keyword():
    return "help"

def helping():
    return f"|{get_keyword()} [Command] - Tells you stuff about the commands"
