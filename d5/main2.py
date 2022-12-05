import re
stacks = []
prepared_stacks = {}

move_compiled = re.compile(r'move (\d+) from (\d+) to (\d+)')

def do_move(hm, f, t):
    items = prepared_stacks[f][:int(hm)]
    prepared_stacks[t] = items + prepared_stacks[t]
    prepared_stacks[f] = prepared_stacks[f][int(hm):]

def combine_stack():
    stack_init_line = stacks.pop()
    stack_names = list(stack_init_line.split())
    stacks_positions = {i: stack_init_line.index(i) for i in stack_names}
    prepared_stacks = {i: [] for i in stacks_positions}
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
    output += v[0]

print(output)
