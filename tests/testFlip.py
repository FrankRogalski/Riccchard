import unittest
import commands.flip as flip
import pandas as pd

class TestFlip(unittest.TestCase):
    def test_use(self):
        cycles = 50000
        series = pd.Series(flip.use(None) for _ in range(cycles))
        self.assertAlmostEqual(len(series[series == "Heads"]) / cycles, 0.4998, delta=0.01)
        self.assertAlmostEqual(len(series[series == "Heads"]) / cycles, 0.4998, delta=0.01)
        self.assertAlmostEqual(len(series[series == "Edge"]) / cycles, 0.0002, delta=0.01)