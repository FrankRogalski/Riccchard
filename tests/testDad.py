import unittest
import commands.dad as dad
from collections import namedtuple

class TestDad(unittest.TestCase):
    def setUp(self):
        self.message = namedtuple("Message", "content")

    def test_random_joke(self):
        message = self.message("|dad cheese")
        dad.use(message)
        