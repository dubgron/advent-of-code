#!/mnt/d/software/python/python.exe -B

import math
import re

input_file = open('day_16_input.txt', 'r')
input_data = input_file.read()

limits = {line[0]: tuple(map(int, line[1:])) for line in re.findall(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$', input_data, re.MULTILINE)}
my_ticket = tuple(map(int, re.findall(r'your ticket:\n((?:\d+,)+\d+)\n', input_data)[0].split(',')))
nearby_tickets = [tuple(map(int, line.split(','))) for line in re.findall(r'nearby tickets:\n((?:(?:\d+,)+\d+\n?)+)', input_data)[0].split('\n')]

def is_good(value, limit):
    return (value >= limit[0] and value <= limit[1]) or (value >= limit[2] and value <= limit[3])

# Part One

min_1 = min([values[0] for name, values in limits.items()])
max_1 = max([values[1] for name, values in limits.items()])
min_2 = min([values[2] for name, values in limits.items()])
max_2 = max([values[3] for name, values in limits.items()])
global_limit = (min_1, max_1, min_2, max_2)

invalid_values = sum([sum([value for value in ticket if not is_good(value, global_limit)]) for ticket in nearby_tickets])
print(invalid_values)

# Part Two

invalid_tickets = []
for ticket in nearby_tickets:
    if not all([is_good(value, global_limit) for value in ticket]):
        invalid_tickets.append(ticket)

for ticket in invalid_tickets:
    nearby_tickets.remove(ticket)

tag_map = {key: [] for key in limits}
for key, limit in limits.items():
    for i in range(len(limits)):
        if all([is_good(value, limit) for value in [ticket[i] for ticket in nearby_tickets]]):
            tag_map[key].append(i)

taken = []
for key, limit in sorted(limits.items(), key=lambda x: len(tag_map[x[0]])):
    tag_map[key] = [tag for tag in tag_map[key] if tag not in taken][0]
    taken.append(tag_map[key])

result = math.prod([my_ticket[tag_map[key]] for key in limits if key.startswith('departure')])
print(result)
