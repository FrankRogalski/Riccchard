import requests

class CanIHazDadJoke:
    def __init__(self):
        self.headers = {"Accept": "application/json", "User-Agent": "Discord bot https://github.com/FrankRogalski/Riccchard"}

    def use(self, msg):
        words = msg.content.split()
        if len(words) <= 1:
            response = requests.get("https://icanhazdadjoke.com", headers=self.headers)
            return response.json()["joke"], True
        else:
            response = requests.get("https://icanhazdadjoke.com/search", params={"limit": 1, "term": " ".join(words[1:])}, headers=self.headers)
            return (res[0]["joke"], True) if len(res := response.json()["results"]) > 0 else ("No jokes found", False)
        
    def get_keyword(self):
        return 'dad'

    def helping(self):
        return f"|{self.get_keyword()} [search term] - tells you a dad joke, related to the search term, if there is one"