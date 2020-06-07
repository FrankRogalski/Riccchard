import unittest
import commands.tuncer as tuncer
import pandas as pd

class TestTuncer(unittest.TestCase):
    def test_use(self):
        cycles = 50000
        series = pd.Series(tuncer.use(None) for _ in range(cycles))
        prob = 1 / len(tuncer.sentences)
        self.assertAlmostEqual(len(series[series == "You are embarrissing me Avan, I am blushing"]) / cycles, prob, delta=0.01)
        self.assertAlmostEqual(len(series[series == "Do I have a mommy Avan?"]) / cycles, prob, delta=0.01)
        self.assertAlmostEqual(len(series[series == "You look nice in that suit Avan"]) / cycles, prob, delta=0.01)
        self.assertAlmostEqual(len(series[series == "Yes, we are in charge, me and my Dad"]) / cycles, prob, delta=0.01)