elves_calories = [0]
index = 0

with open('input') as f:
    for line in f:
        if line == '\n':
           index += 1
           elves_calories.append(0)
           continue
        elves_calories[index] += int(line)

elves_calories.sort()

print(elves_calories[-1])
print(sum(elves_calories[-3:]))
