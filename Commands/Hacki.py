import random

counter = 0
responses = ("Was?!?!?", "huh", "wa", "wie")

def use(msg):
    global counter
    counter += 1
    if random.random() > 1 / (counter + 0.5):
        counter = 0
        return random.choice(responses), False
    return "...", False

def get_keyword():
    return 'hacki'

def helping():
    return f"|{get_keyword()} - Wakes up... if you are lucky"
