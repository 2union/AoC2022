import re
from collections import deque
stacks = []
prepared_stacks = {}

move_compiled = re.compile(r'move (\d+) from (\d+) to (\d+)')

def do_move(hm, f, t):
    for i in range(0, int(hm)):
        item = prepared_stacks[f].popleft()
        prepared_stacks[t].appendleft(item)

def combine_stack():
    stack_init_line = stacks.pop()
    stack_names = list(stack_init_line.split())
    stacks_positions = {i: stack_init_line.index(i) for i in stack_names}
    prepared_stacks = {i: deque() for i in stacks_positions}
    for l in stacks:
        for name, position in stacks_positions.items():
            if l[position] != ' ':
            	prepared_stacks[name].append(l[position])
    return prepared_stacks

with open('input') as f:
    stack_full = False
    for i in f:
        if i == "\n":
            stack_full = True
            prepared_stacks = combine_stack()
        if not stack_full:
            stacks.append(i)
        else:
            match = move_compiled.match(i)
            if match:
                do_move(match.group(1), match.group(2), match.group(3))

output = ''
for i, v in prepared_stacks.items():
    output += v.popleft()

print(output)
