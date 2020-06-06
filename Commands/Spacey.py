class Spacey:
    def use(self, msg):
        return "We are in the Universe! Planets live inside the moon! A rocket ship can go to space, a rocket ship can go to the moon!", True

    def get_keyword(self):
        return "spacey"

    def helping(self):
        return f"|{self.get_keyword()} - Sings a lovely song"
