import random


class Tuncer:
    def use(self, msg):
        return random.choice(["You are embarrissing me Avan, I am blushing", "Do I have a mommy Avan?",
            "You look nice in that suit Avan", "You are embarrissing me Avan, I am blushing",
            "Yes, we are in charge, me and my Dad"]), False

    def get_keyword(self):
        return 'tuncer'

    def helping(self):
            return f"|{self.get_keyword()} - Classic qoutes from Tuncer"
