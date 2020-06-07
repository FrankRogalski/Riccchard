import unittest
import commands.repeat as repeat
from collections import namedtuple

message = namedtuple("Message", "content")

class TestRepeat(unittest.TestCase):
    def test_use(self):
        msg = message("repeat moin, hallo")
        self.assertEqual("moin, hallo", repeat.use(msg))

    def test_use_no_message(self):
        msg = message("repeat")
        self.assertEqual("Please type a message, that can be repeated", repeat.use(msg))