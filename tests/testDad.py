import unittest
import commands.dad as dad
from collections import namedtuple

class TestDad(unittest.TestCase):
    def setUp(self):
        self.message = namedtuple("Message", "content")

    def test_cheese_joke(self):
        message = self.message("|dad cheese")
        self.assertIn("cheese", dad.use(message)[0])
        
    def test_random_joke(self):
        message = self.message("|dad cheese")
        self.assertEqual(str, type(dad.use(message)[0]))
        