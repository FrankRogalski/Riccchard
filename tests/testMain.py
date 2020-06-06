import unittest
from collections import namedtuple

def on_message(message):
    i = message.content.find(" ")
    command = commands.get(message.content[1:(i + 1 if i != -1 else len(message.content))])
    if command and message.content.startswith("|"):
        ans = command.use(message)

message = namedtuple("Message", "content")
on_message(message("|dad cheese"))
