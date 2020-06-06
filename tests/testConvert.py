import unittest
from Commands.Convert import Convert
from collections import namedtuple

class TestConvert(unittest.TestCase):
    def setUp(self):
        self.convert = Convert()
        self.message = namedtuple("Message", "content")

    def test_get_keyword(self):
        self.assertEqual("convert", self.convert.get_keyword())

    def test_helping(self):
        self.assertEqual("|convert <Numeral system'to'Numeral system> <number> - Converts numbers between two numeral systems", self.convert.helping())

    def test_use_wrong_argument_number(self):
        message = self.message("convert 1")
        self.assertEqual(("Wrong number of arguments. This is the Syntax: |convert <Numeral system'to'Numeral system> <number> - Converts numbers between two numeral systems", False), 
            self.convert.use(message))

    def test_use_wrong_number_system(self):
        message = self.message("convert 1ato2 20")
        self.assertEqual(("Conversion Error. Please make shure your bases aren't bigger than 36 and that your input matches the base", False), self.convert.use(message))

    def test_use_to_big_number_system(self):
        message = self.message("convert 100to2 20")
        self.assertEqual(("Conversion Error. Please make shure your bases aren't bigger than 36 and that your input matches the base", False), self.convert.use(message))

    def test_use_success(self):
        message = self.message("convert 10to2 20")
        self.assertEqual(("10100", False), self.convert.use(message))
