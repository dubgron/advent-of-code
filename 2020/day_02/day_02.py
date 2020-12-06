#!/mnt/d/software/python/python.exe -B

import re

# Part One

input_file = open('day_02_input.txt', 'r')
input_data = re.findall(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$', input_file.read(), re.MULTILINE)

err = 0

for line in input_data:
    (rep_min, rep_max, letter, pwd) = line
    count = pwd.count(letter)

    err += (count >= int(rep_min) and count <= int(rep_max))

print(err)

# Part Two

err = 0

for line in input_data:
    (pos_1, pos_2, letter, pwd) = line

    err += bool(pwd[int(pos_1) - 1] == letter) ^ bool(pwd[int(pos_2) - 1] == letter)

print(err)
