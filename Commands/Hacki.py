import random
import discord.message
from typing import Tuple, Union

counter = 0
responses = ("Was?!?!?", "huh", "wa", "wie")
keyword = 'hacki'
helping = f"|{keyword} - Wakes up... if you are lucky"

def use(message: discord.message) -> Union[str, Tuple[str, bool]]:
    global counter
    counter += 1
    if random.random() > 1 / (counter + 0.5):
        counter = 0
        return random.choice(responses), True
    return "..."
