# # Part 1
# puzzle_input = open("day-03-input.txt")

# res = 0

# for rucksack in puzzle_input:
#     rucksack = rucksack.rstrip()
#     dupe = list(set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:]))[0]
#     if dupe.isupper():
#         res += ord(dupe)-38
#     elif dupe.islower():
#         res += ord(dupe)-96

# print(res)
# puzzle_input.close()

# Part 2
puzzle_input = open("day-03-input.txt")

rucksacks = puzzle_input.readlines()
res = 0

for i in range(0,len(rucksacks),3):
    group = rucksacks[i:i+3]
    badge = list(set(group[0].rstrip())&set(group[1].rstrip())&set(group[2].rstrip()))[0]
    if badge.isupper():
        res += ord(badge)-38
    elif badge.islower():
        res += ord(badge)-96
    
print(res)

puzzle_input.close()