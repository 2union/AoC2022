
import re
from enum import Enum

command_ex = re.compile(r'(\w) (\d+)')

nodes = [complex(0, 0)] * 10
nodes_positions = {nodes[-1]}

class Direction(Enum):
    U = complex(0, 1)
    D = complex(0, -1)
    R = complex(1, 0)
    L = complex(-1, 0)

def point_pos(point):
    if not point:
        return 0
    return point // abs(point)

def move(diff):
    if abs(diff) >= 2:
        return complex(point_pos(diff.real), point_pos(diff.imag))
    return complex(0, 0)

def do_command(command, value):
    global head_position
    for _ in range(value):
        nodes[0] += Direction[command].value
        for i in range(1, len(nodes)):
            nodes[i] += move(nodes[i-1] - nodes[i])
        nodes_positions.add(nodes[-1])

with open('input') as f:
    for line in f:
        matches = command_ex.match(line)
        do_command(matches.group(1), int(matches.group(2)))

print(len(nodes_positions))
