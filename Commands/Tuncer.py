import random
import discord.message

keyword = "tuncer"
helping = f"|{keyword} - Classic qoutes from Tuncer"

def use(message: discord.message) -> str:
    return random.choice(["You are embarrissing me Avan, I am blushing", "Do I have a mommy Avan?",
        "You look nice in that suit Avan", "You are embarrissing me Avan, I am blushing",
        "Yes, we are in charge, me and my Dad"])
