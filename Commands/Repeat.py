keyword = "repeat"
helping = f"|{keyword} <some sentence> - Repeats the sentence"

def use(msg):
    return " ".join(msg[1:]) if len(msg := msg.content.split(" ")) > 1 else "Please type a message, that can be repeated"
