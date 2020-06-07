import unittest
import commands.spacey as spacey

class TestSpacey(unittest.TestCase):
    def test_use(self):
        self.assertEqual(("We are in the Universe! Planets live inside the moon! A rocket ship can go to space, a rocket ship can go to the moon!", True), spacey.use(None))