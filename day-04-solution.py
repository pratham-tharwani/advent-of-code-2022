# Part 1
puzzle_input = open('day-04-input.txt')

res = 0

for pair in puzzle_input:
    pair = pair.rstrip().split(',')
    a = list(map(int, pair[0].split('-')))
    b = list(map(int, pair[1].split('-')))
    if a[0] <= b[0] <= b[1] <= a[1] or b[1] >= a[1] >= a[0] >= b[0]:
        res += 1   

print(res)

puzzle_input.close()

# Part 2
puzzle_input = open('day-04-input.txt')

res = 0

for pair in puzzle_input:
    pair = pair.rstrip().split(',')
    a = list(map(int, pair[0].split('-')))
    b = list(map(int, pair[1].split('-')))
    if (a[0] <= b[0] and a[1] >= b[0]) or (a[0] >= b[0] and a[0] <= b[1]):
        res += 1

print(res)

puzzle_input.close()