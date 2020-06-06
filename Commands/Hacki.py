import random

counter = 0
responses = ("Was?!?!?", "huh", "wa", "wie")
keyword = 'hacki'
helping = f"|{keyword} - Wakes up... if you are lucky"

def use(msg):
    global counter
    counter += 1
    if random.random() > 1 / (counter + 0.5):
        counter = 0
        return random.choice(responses)
    return "..."
