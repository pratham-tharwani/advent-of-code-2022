import re

# Part 1
puzzle_input = open('day-05-input.txt')

stacks = [[] for _ in range(len(puzzle_input.readline())//4)]

puzzle_input.seek(0)

for line in puzzle_input:
    line = line.rstrip()
    if not line.startswith('move'):
        for i in range(1, len(line), 4):
            if line[i].isalpha() and line[i] != ' ':
                stacks[i//4].insert(0, line[i])

def move_crates(count, src, dest):
    global stacks

    for _ in range(count):
        stacks[dest-1].append(stacks[src-1].pop(-1))

puzzle_input.seek(0)

for line in puzzle_input:
    line = line.rstrip().lstrip()
    if line.startswith('move'):
        args = re.split('move | from | to ', line)
        args.pop(0)
        args = list(map(int, args))
        move_crates(*args)

res = ''
for stack in stacks:
    res += stack[-1]

print(res)
puzzle_input.close()

# Part 2
puzzle_input = open('day-05-input.txt')

stacks = [[] for _ in range(len(puzzle_input.readline())//4)]

puzzle_input.seek(0)

for line in puzzle_input:
    line = line.rstrip()
    if not line.startswith('move'):
        for i in range(1, len(line), 4):
            if line[i].isalpha() and line[i] != ' ':
                stacks[i//4].insert(0, line[i])


def move_crates_9001(count, src, dest):
    global stacks
    stacks[dest-1].extend(stacks[src-1][-count:])
    del(stacks[src-1][-count:])

puzzle_input.seek(0)

for line in puzzle_input:
    line = line.rstrip().lstrip()
    if line.startswith('move'):
        args = re.split('move | from | to ', line)
        args.pop(0)
        args = list(map(int, args))
        move_crates_9001(*args)

res = ''
for stack in stacks:
    res += stack[-1]

print(res)
puzzle_input.close()