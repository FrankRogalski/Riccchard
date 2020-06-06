import random

options = ("Heads", "Tails")

def use(msg):
    return ("Edge", False) if random.random() < 0.0002 else (random.choice(options), False)

def get_keyword():
    return "flip"

def helping():
    return f"|{get_keyword()} - A simple flip of a coin"
