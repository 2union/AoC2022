from collections import deque

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
hights = {a: v for v, a in enumerate(ascii_lowercase)}

start_pos = complex(0, 0)
finish_pos = complex(0, 0)

sizes = []
with open('input') as f:
    for l, line in enumerate(f):
        line_heights = []
        for i, char in enumerate(line.strip()):
            if char == 'S':
                start_pos = complex(i, l)
                line_heights.append(0)
            elif char == 'E':
                finish_pos = complex(i, l)
                line_heights.append(len(ascii_lowercase)-1)
            else:
                line_heights.append(hights[char])
        sizes.append(line_heights)

visited = {start_pos}
queue = deque()
queue.append(start_pos)
backtrack = {}

def get_points(point):
    points = []
    if point.imag-1 >= 0:
        points.append(point + complex(0, -1))
    if point.imag+1 <= len(sizes)-1:
        points.append(point + complex(0, 1))
    if point.real-1 >= 0:
        points.append(point + complex(-1, 0))
    if point.real+1 <= len(sizes[0])-1:
        points.append(point + complex(1, 0))
    return points

while queue:
    curent = queue.popleft()
    hight = sizes[int(curent.imag)][int(curent.real)]
    points = get_points(curent)

    for point in points:
        if point in visited:
            continue
        point_height = sizes[int(point.imag)][int(point.real)]
        if point_height - hight > 1:
            continue

        visited.add(point)
        backtrack[point] = curent
        queue.append(point)

        if point == finish_pos:
            queue = deque()
            break


track = [finish_pos]
pointer = finish_pos
while pointer != start_pos:
    pointer = backtrack.get(pointer, start_pos)
    track.append(pointer)

print(len(track)-1)
