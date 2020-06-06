class Say:
    def use(self, msg):
        return (" ".join(msg[1:]), True) if len(msg := msg.content.split(" ")) > 1 else ("Please type a message, that can be repeated", False)

    def get_keyword(self):
        return 'say'

    def helping(self):
        return f"|{self.get_keyword()} <some sentence> - Speaks the sentence"
