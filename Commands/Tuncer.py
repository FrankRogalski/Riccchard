import random
import discord.message

keyword = "tuncer"
helping = f"|{keyword} - Classic qoutes from Tuncer"
sentences = ("You are embarrissing me Avan, I am blushing", "Do I have a mommy Avan?",
        "You look nice in that suit Avan", "Yes, we are in charge, me and my Dad")

def use(message: discord.message) -> str:
    return random.choice(sentences)
