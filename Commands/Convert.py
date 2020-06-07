import sys
import discord.message
from collections import namedtuple

keyword = "convert"
helping = f"|{keyword} <Numeral system'to'Numeral system> <number> - Converts numbers between two numeral systems"
systems = namedtuple("Systems", "start goal")

def turn_ord(system: int) -> "function":
    def start(digit: str) -> int:
        try:
            digit = int(digit) 
        except ValueError:
            digit = ord(digit.upper()) - 55
        if digit > 35 or digit >= system: raise ValueError()
        return digit
    return start

def validate(i: str) -> int:
    i = int(i)
    if i < 2 or i > 36: raise ValueError()
    return i

def get_systems(system_string: str) -> systems:
    return systems(*(validate(i) for i in system_string.split("to")))

def use(message: discord.message) -> str:
    msg = message.content.split()[1:]
    if len(msg) != 2:
        return f"Wrong number of arguments. This is the Syntax: {helping()}"

    try:
        systems = get_systems(msg[0])
        start = list(map(turn_ord(systems.start), msg[1]))
    except ValueError:
        return "Conversion Error. Please make shure your bases aren't bigger than 36 and that your input matches the base"

    summe = sum(int(i) * systems.start ** power for power, i in enumerate(start[::-1]))

    if summe > sys.float_info.max or summe < sys.float_info.min:
        return "Das result is to small/big"

    rest = []
    while summe > 0:
        rest.append(summe % systems.goal)
        summe //= systems.goal

    return "".join(chr(i + 55) if i > 9 else str(i) for i in rest)[::-1]
