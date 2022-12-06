from collections import deque

last_for = deque()
position = 0

with open('input') as f:
    buffer =  f.read()
    for i, c in enumerate(buffer):
        last_for.append(c)
        if len(last_for) > 4:
            last_for.popleft()
        if len(set(last_for)) == 4:
            position = i+1
            break

print(position)
