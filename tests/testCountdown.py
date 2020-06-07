import unittest
import commands.countdown as countdown
from collections import namedtuple

message = namedtuple("Message", "content")

class TestCountdown(unittest.TestCase):
    def test_use(self):
        msg = message("countdown 3 moin")
        self.assertEqual(("3\n2\n1\nmoin", True), countdown.use(msg))

    def test_use_no_end(self):
        msg = message("countdown 3")
        self.assertEqual(("3\n2\n1\ndone", True), countdown.use(msg))

    def test_use_no_arguments(self):
        msg = message("countdown")
        self.assertEqual("please specify a number to count down from", countdown.use(msg))

    def test_use_nan(self):
        msg = message("countdown a")
        self.assertEqual("that's not a valid number", countdown.use(msg))
        