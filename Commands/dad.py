import requests

headers = {"Accept": "application/json", "User-Agent": "Discord bot https://github.com/FrankRogalski/Riccchard"}
keyword = "dad"
helping = f"|{keyword} [search term] - tells you a dad joke, related to the search term, if there is one"

def use(msg):
    words = msg.content.split()
    if len(words) <= 1:
        response = requests.get("https://icanhazdadjoke.com", headers=headers)
        return response.json()["joke"], True
    else:
        response = requests.get("https://icanhazdadjoke.com/search", params={"limit": 1, "term": " ".join(words[1:])}, headers=headers).json()["results"]
        return (response[0]["joke"], True) if response else ("No jokes found", False)