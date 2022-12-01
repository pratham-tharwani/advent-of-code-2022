# Part 1
puzzle_input = open("day-01-input.txt")

curr_total = max_calories = 0

for line in puzzle_input:
    if line == '\n':
        if curr_total > max_calories:
            max_calories = curr_total
        curr_total = 0
    else:
        curr_total += int(line.strip())

print(max_calories)

puzzle_input.close()

# Part 2
puzzle_input = open("day-01-input.txt")

curr_total = max_1 = max_2 = max_3 = 0

for line in puzzle_input:
    if line == '\n':
        if curr_total > max_1:
            max_2, max_3 = max_1, max_2
            max_1 = curr_total
        elif curr_total > max_2:
            max_3 = max_2
            max_2 = curr_total
        elif curr_total > max_3:
            max_3 = curr_total
        curr_total = 0
    else:
        curr_total += int(line.strip())

print(max_1+ max_2 + max_3)

puzzle_input.close()