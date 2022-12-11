import re
from enum import Enum


class Sprite(tuple):
    def __add__(self, other):
        return Sprite(i + other for i in self)
    def __sub__(self, other):
        return Sprite(i - other for i in self)

instruction_ex = re.compile(r'(\w{4})( (.*))?$')

class Instructions(Enum):
    addx = 2
    noop = 1

ticks = -1
def frequency_generator(instruction):
    global ticks
    for i in range(Instructions[instruction].value):
        ticks += 1
        yield ticks

sprite_position = Sprite([0, 1, 2])
crt_row = ''

with open('input') as f:
    for line in f:
        matches = instruction_ex.match(line)
        instruction = matches.group(1)
        for tick in frequency_generator(instruction):
            if tick%40 in sprite_position:
                crt_row += '#'
            else:
                crt_row += '.'
        if instruction == 'addx':
            move = int(matches.group(3))
            sprite_position += move

for i in range(40, 260, 40):
    print(crt_row[i-40:i])
