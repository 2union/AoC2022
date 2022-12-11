import re
from enum import Enum

command_ex = re.compile(r'(\w) (\d+)')

head_position = complex(0, 0)
tail_position = complex(0, 0)
tail_positions = {tail_position}

class Direction(Enum):
    U = complex(0, 1)
    D = complex(0, -1)
    R = complex(1, 0)
    L = complex(-1, 0)

def point_pos(point):
    if not point:
        return 0
    return point // abs(point)

def move_tail():
    global tail_position, tail_positions
    if abs(diff := (head_position - tail_position)) >= 2:
        tail_position += complex(point_pos(diff.real), point_pos(diff.imag))
        tail_positions.add(tail_position)

def do_command(command, value):
    global head_position
    for _ in range(value):
        head_position += Direction[command].value
        move_tail()

with open('input') as f:
    for line in f:
        matches = command_ex.match(line)
        do_command(matches.group(1), int(matches.group(2)))

print(len(tail_positions))
