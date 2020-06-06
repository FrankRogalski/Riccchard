import sys
from collections import namedtuple

class Convert:
    def __is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __turn_ord(self, system):
        def start(digit):
            nonlocal system
            digit = int(digit) if self.__is_number(digit) else ord(digit.upper()) - 55
            if digit > 35 or digit >= system: raise ValueError()
            return digit
        return start

    def __validate(self, i):
        i = int(i)
        if i < 2 or i > 36: raise ValueError()
        return i

    def __get_systems(self, system_string):
        return namedtuple("Systems", "start goal")(*(self.__validate(i) for i in system_string.split("to")))

    def use(self, msg):
        contents = msg.content.split(" ")
        if len(contents) != 3:
            return f"Wrong number of arguments. This is the Syntax: {self.helping()}", False

        try:
            systems = self.__get_systems(contents[1])
            start = list(map(self.__turn_ord(systems.start), contents[2]))
        except ValueError:
            return "Conversion Error. Please make shure your bases aren't bigger than 36 and that your input matches the base", False

        summe = sum(int(i) * systems.start ** power for power, i in enumerate(start[::-1]))

        if summe > sys.float_info.max or summe < sys.float_info.min:
            return "Das result is to small/big", False

        rest = []
        while summe > 0:
            rest.append(summe % systems.goal)
            summe //= systems.goal

        return "".join(chr(i + 55) if i > 9 else str(i) for i in rest)[::-1], False

    def get_keyword(self):
        return "convert"

    def helping(self):
        return f"|{self.get_keyword()} <Numeral system'to'Numeral system> <number> - Converts numbers between two numeral systems"
