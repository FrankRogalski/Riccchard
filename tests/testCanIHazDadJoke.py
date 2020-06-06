import unittest
from Commands.CanIHazDadJoke import CanIHazDadJoke
from collections import namedtuple

class TestCanIHazDadJoke(unittest.TestCase):
    def setUp(self):
        self.canIHazDadJoke = CanIHazDadJoke()
        self.message = namedtuple("Message", "content")

    def test_random_joke(self):
        message = self.message("|dad cheese")
        self.canIHazDadJoke.use(message)
        