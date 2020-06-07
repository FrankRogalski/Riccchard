import unittest
import commands.hacki as hacki
import pandas as pd

class TestHacki(unittest.TestCase):
    def test_use(self):
        cycles = 50000
        series = pd.Series(hacki.use(None) for _ in range(cycles))
        self.assertAlmostEqual(len(series[series == "..."]) / cycles, 0.51, delta=0.01)