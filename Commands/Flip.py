import random
import discord.message

options = ("Heads", "Tails")
keyword = "flip"
helping = f"|{keyword} - A simple flip of a coin"

def use(message: discord.message) -> str:
    return "Edge" if random.random() < 0.0002 else random.choice(options)
