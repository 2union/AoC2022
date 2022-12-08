def clean_stack(stack, cut_line):
    cleaned_stack = []
    for i in stack:
        if i[1] > cut_line:
            cleaned_stack.append(i)
    return cleaned_stack

trees = []
beauty_matrix = []

with open('input') as f:
    line_len = 0
    col_max = []
    visible_matrix = []
    bottom_stack = []
    lines_count = 0
    for i, line in enumerate(f):
        line_striped = line.strip()
        line_len = len(line_striped)
        trees.append(list(map(int, line_striped)))
        beauty_matrix.append([0]*line_len)
        if i == 0:
            col_max = list(map(int, line_striped))
            visible_matrix.append([0]*line_len)
            bottom_stack = list(map(lambda n: [n], enumerate(col_max)))
            continue

        right_stack = []
        line_max = int(line_striped[0])
        matrix_line = [1] + [0] * (line_len - 1)

        for j, height in enumerate(map(int, line_striped)):
            if j > 0 and right_stack[-1][1] <= height:
                right_stack = clean_stack(right_stack, height)
            right_stack.append((j, height))

            if bottom_stack[j][-1][1] <= height:
                bottom_stack[j] = clean_stack(bottom_stack[j], height)
            bottom_stack[j].append((i, height))

            if height > line_max:
                line_max = height
                matrix_line[j] = 1

            if height > col_max[j]:
                col_max[j] = height
                matrix_line[j] = 1

            if j in [0, (line_len - 1)]:
                matrix_line[j] = 0

        right_stack_size = len(right_stack)

        for i in right_stack:
            if i[0] not in [0, (line_len - 1)]:
                matrix_line[i[0]] = 1

        visible_matrix.append(matrix_line)

    for i, heights in enumerate(bottom_stack):
        for j in heights:
            if i not in [0, (line_len - 1)]:
                visible_matrix[j[0]][i] = 1

    visible_matrix.pop()
    visible_matrix.append([0]*line_len)

    for i, line in enumerate(visible_matrix):
        for j, visible in enumerate(line):
            if not visible:
                continue
            max_top = i
            max_left = j
            top = max_top
            left = max_left
            bottom = 0
            right = 0
            height = trees[i][j]
            for l, line in enumerate(trees):
                if l < i:
                    if line[j] >= height:
                        top = max_top - l
                if l == i:
                   for p, tree in enumerate(line):
                       if p < j:
                           if tree >= height:
                               left = max_left - p
                       if p > j:
                           right += 1
                           if tree >= height:
                               break
                if l > i:
                   bottom += 1
                   if line[j] >= height:
                       break

            beauty_matrix[i][j] = top*bottom*left*right

    print(max(map(max, beauty_matrix)))
