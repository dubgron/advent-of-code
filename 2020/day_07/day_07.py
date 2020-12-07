#!/mnt/d/software/python/python.exe -B

import re

input_file = open('day_07_input.txt', 'r')
input_data = input_file.read()

# Part One

my_bag = 'shiny gold'
bags = set()

data = re.sub(r' bags contain \d+ ', r',', input_data)
data = re.sub(r' bags?, \d+ ', r',', data)
data = re.sub(r' bags?\.', r'', data)
data = [line.split(',') for line in data.split('\n')]

for i in range(len(data)):
    for line in data[i::-1]:
        outside = line[0]
        inside = line[1:]
        if my_bag in inside or bags & set(inside):
            bags.add(outside)

print(len(bags))

# Part Two

bags = { 'no other': [] }

data = re.sub(r' bags contain (\d+) ', r',\1:', input_data)
data = re.sub(r' bags contain no other', r',0:no other', data)
data = re.sub(r' bags?, (\d+) ', r',\1:', data)
data = re.sub(r' bags?\.', r'', data)
data = [line.split(',') for line in data.split('\n')]

for line in data:
    outside = line[0]
    inside = [p.split(':')[::-1] for p in line[1:]]
    bags[outside] = [(item[0], int(item[1])) for item in inside]

def total(bags_list):
    result = 0
    for item in bags_list:
        result += item[1] * (1 + total(bags[item[0]]))
    return result

print(total(bags[my_bag]))
