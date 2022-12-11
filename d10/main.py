import re
from enum import Enum

instruction_ex = re.compile(r'(\w{4})( (.*))?$')

class Instructions(Enum):
    addx = 2
    noop = 1

ticks = 0
def frequency_generator(instruction):
    global ticks
    for i in range(Instructions[instruction].value):
        ticks += 1
        yield ticks

x = 1
results = []
with open('input') as f:
    for line in f:
        matches = instruction_ex.match(line)
        instruction = matches.group(1)
        for tick in frequency_generator(instruction):
            if tick == 20 or ((tick - 20) % 40 == 0):
                results.append(x*tick)
        if instruction == 'addx':
            move = int(matches.group(3))
            x += move

print(sum(results))
