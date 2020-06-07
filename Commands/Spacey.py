import discord.message
from typing import Tuple

keyword = "spacey"
helping = f"|{keyword} - Sings a lovely song"

def use(message: discord.message) -> Tuple[str, bool]:
    return "We are in the Universe! Planets live inside the moon! A rocket ship can go to space, a rocket ship can go to the moon!", True
