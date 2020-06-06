keyword = "say"
helping = f"|{keyword} <some sentence> - Speaks the sentence"

def use(msg):
    return (" ".join(msg[1:]), True) if len(msg := msg.content.split(" ")) > 1 else ("Please type a message, that can be repeated", False)
