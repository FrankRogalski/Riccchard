
def use(message):
    split = message.content.split()
    if len(split) <= 1:
        return "please specify a number to count down from", False
    try:
        return "\n".join(map(str, range(int(split[1]), 0, -1))) + "\n" + splitted(split), True
    except ValueError:
        return "that's not a valid number", False

def splitted(split):
    return " ".join(split[2:]) if len(split) > 2 else "done"

def get_keyword():
    return "countdown"

def helping():
    return f"|{get_keyword()} <number>, counts down from a given number"