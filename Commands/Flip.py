import random

options = ("Heads", "Tails")
keyword = "flip"
helping = f"|{keyword} - A simple flip of a coin"

def use(msg):
    return "Edge" if random.random() < 0.0002 else random.choice(options)
