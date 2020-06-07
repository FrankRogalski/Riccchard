import unittest
import commands.say as say
from collections import namedtuple

message = namedtuple("Message", "content")

class TestSay(unittest.TestCase):
    def test_use(self):
        msg = message("repeat moin, hallo")
        self.assertEqual(("moin, hallo", True), say.use(msg))

    def test_use_no_message(self):
        msg = message("repeat")
        self.assertEqual("Please type a message, that can be repeated", say.use(msg))