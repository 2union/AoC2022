from collections import deque

last_forteen = deque()
position = 0

with open('input') as f:
    buffer =  f.read()
    for i, c in enumerate(buffer):
        last_forteen.append(c)
        if len(last_forteen) > 14:
            last_forteen.popleft()
        if len(set(last_forteen)) == 14:
            position = i+1
            break

print(position)
