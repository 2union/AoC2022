def clean_stack(stack, cut_line):
    cleaned_stack = []
    for i in stack:
        if i[1] > cut_line:
            cleaned_stack.append(i)
    return cleaned_stack

with open('input') as f:
    line_len = 0
    col_max = []
    visible_matrix = []
    bottom_stack = []
    for i, line in enumerate(f):
        line_striped = line.strip()

        if i == 0:
            line_len = len(line_striped)
            col_max = list(map(int, line_striped))
            visible_matrix.append([1]*line_len)
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
        right_stack_size = len(right_stack)

        for i in right_stack:
            matrix_line[i[0]] = 1

        visible_matrix.append(matrix_line)

    for i, heights in enumerate(bottom_stack):
        for j in heights:
            visible_matrix[j[0]][i] = 1

    visible_matrix.pop()
    visible_matrix.append([1]*line_len)

    print(sum(map(sum, visible_matrix)))
