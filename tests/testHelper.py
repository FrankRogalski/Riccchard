import unittest
import commands.helper as helper
from collections import namedtuple

message = namedtuple("Message", "content")
class_ = namedtuple("Class", "helping")

helper.classes = {"test": class_("this is a test"), "help": helper}

class TestHelper(unittest.TestCase):
    def test_use(self):
        msg = message("help")
        self.assertEqual("```this is a test\n|help [Command] - Tells you stuff about the commands```", helper.use(msg))
        
    def test_use_wron_keyword(self):
        msg = message("help non")
        self.assertEqual("```this is a test\n|help [Command] - Tells you stuff about the commands```", helper.use(msg))

    def test_use_keyword(self):
        msg = message("help test")
        self.assertEqual("```this is a test```", helper.use(msg))