def use(msg):
    return " ".join(msg[1:]) if len(msg := msg.content.split(" ")) > 1 else "Please type a message, that can be repeated", False

def get_keyword():
    return 'repeat'

def helping():
    return f"|{get_keyword()} <some sentence> - Repeats the sentence"
