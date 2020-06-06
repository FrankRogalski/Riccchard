import requests

class CanIHazDadJoke:
    def use(self, msg):
        words = msg.content.split()
        if len(words) <= 1:
            response = requests.get("https://icanhazdadjoke.com", headers={"Accept": "application/json"})
            return response.json()["joke"], True
        else:
            response = requests.get("https://icanhazdadjoke.com/search", params={"limit": 1, "term": " ".join(words[1:])}, headers={"Accept": "application/json"})
            return (res[0]["joke"], True) if len(res := response.json()["results"]) > 0 else ("No jokes found", False)
        
    def get_keyword(self):
        return 'dad'

    def helping(self):
        return f"|{self.get_keyword()} [search term] - tells you a dad joke, related to the search term, if there is one"