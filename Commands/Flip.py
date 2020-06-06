import random

class Flip:
    def __init__(self):
        self.options = ("Heads", "Tails")

    def use(self, msg):
        return ("Edge", False) if random.random() < 0.0002 else (random.choice(self.options), False)

    def get_keyword(self):
        return "flip"

    def helping(self):
        return f"|{self.get_keyword()} - A simple flip of a coin"
