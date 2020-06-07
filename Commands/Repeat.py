import discord.message

keyword = "repeat"
helping = f"|{keyword} <some sentence> - Repeats the sentence"

def use(message: discord.message) -> str:
    msg = message.content.split()[1:]
    return " ".join(msg) if msg else "Please type a message, that can be repeated"
