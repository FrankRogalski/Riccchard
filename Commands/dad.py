import requests
import discord.message
from typing import Tuple, Union

headers = {"Accept": "application/json", "User-Agent": "Discord bot https://github.com/FrankRogalski/Riccchard"}
keyword = "dad"
helping = f"|{keyword} [search term] - tells you a dad joke, related to the search term, if there is one"

def use(message: discord.message) -> Union[str, Tuple[str, bool]]:
    msg = message.content.split()[1:]
    if not msg:
        response = requests.get("https://icanhazdadjoke.com", headers=headers)
        return response.json()["joke"], True
    else:
        response = requests.get("https://icanhazdadjoke.com/search", params={"limit": 1, "term": " ".join(msg)}, headers=headers).json()["results"]
        return (response[0]["joke"], True) if response else "No jokes found"