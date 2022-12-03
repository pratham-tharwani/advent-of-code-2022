# Part 1
puzzle_input = open("day-02-input.txt")

score = 0
points_table = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

for round in puzzle_input:
    score += points_table[round.rstrip()]

print(score)

puzzle_input.close()

# Part 2
puzzle_input = open("day-02-input.txt")

score = 0
points_table = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

for round in puzzle_input:
    score += points_table[round.rstrip()]

print(score)

puzzle_input.close()