#!/mnt/d/software/python/python.exe -B

input_file = open('day_03_input.txt', 'r')
input_data = input_file.readlines()
input_size = len(input_data)

LINE_LENGTH = len(input_data[0]) - 1

# Part One

trees = 0
x = 0

for line in input_data:
    trees += (line[x % LINE_LENGTH] == '#')
    x += 3

print(trees)

# Part Two

import math

move_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_total = []

for move in move_list:
    trees = 0
    x = 0
    for y in range(0, input_size, move[1]):
        line = input_data[y]
        trees += (line[x % LINE_LENGTH] == '#')
        x += move[0]

    trees_total.append(trees)

print(math.prod(trees_total))
