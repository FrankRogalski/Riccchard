import random

class Flip:
    def use(self, msg):
        if random.random() < 0.0002:
            return "Edge"
        return random.choice(["Heads", "Tails"]), False

    def get_keyword(self):
        return "flip"

    def helping(self):
        return f"|{self.get_keyword()} - A simple flip of a coin"
