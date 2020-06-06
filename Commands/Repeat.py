class Repeat:
    def use(self, msg):
        return " ".join(msg[1:]) if (msg := msg.content.split(" ")) > 1 else  "Please type a message, that can be repeated", False

    def get_keyword(self):
        return 'repeat'

    def helping(self):
        return f"|{self.get_keyword()} <some sentence> - Repeats the sentence"
