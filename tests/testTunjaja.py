import unittest
import commands.tunjaja as tunjaja

class TestTunjaja(unittest.TestCase):
    def test_use(self):
        self.assertEqual("lol", tunjaja.use(None))