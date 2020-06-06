keyword = "countdown"
helping = f"|{keyword} <number>, counts down from a given number"

def use(message):
    split = message.content.split()
    if len(split) <= 1:
        return "please specify a number to count down from"
    try:
        return "\n".join(map(str, range(int(split[1]), 0, -1))) + "\n" + splitted(split), True
    except ValueError:
        return "that's not a valid number"

def splitted(split):
    return " ".join(split[2:]) if len(split) > 2 else "done"
