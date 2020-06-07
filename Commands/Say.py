import discord.message
from typing import Union, Tuple

keyword = "say"
helping = f"|{keyword} <some sentence> - Speaks the sentence"

def use(message: discord.message) -> Union[str, Tuple[str, bool]]:
    msg = message.content.split()[1:]
    return (" ".join(msg), True) if msg else "Please type a message, that can be repeated"
