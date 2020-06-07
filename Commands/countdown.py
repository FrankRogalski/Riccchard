from typing import List, Union, Tuple
import discord.message

keyword = "countdown"
helping = f"|{keyword} <number>, counts down from a given number"

def use(message: discord.message) -> Union[str, Tuple[str, bool]]:
    msg = message.content.split()[1:]
    if not msg:
        return "please specify a number to count down from"
    try:
        return "\n".join(map(str, range(int(msg[0]), 0, -1))) + "\n" + splitted(msg), True
    except ValueError:
        return "that's not a valid number"

def splitted(msg: List[str]) -> str:
    return " ".join(msg[1:]) if len(msg) > 1 else "done"
