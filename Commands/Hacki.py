import random

class Hacki:
    def __init__(self):
        self.__counter = 0

    def use(self, msg):
        self.__counter += 1
        if random.random() > 1 / (self.__counter + 0.5):
            self.__counter = 0
            return random.choice(["Was?!?!?", "huh", "wa", "wie"]), False
        return "...", False

    def get_keyword(self):
        return 'hacki'

    def helping(self):
        return f"|{self.get_keyword()} - Wakes up... if you are lucky"
