#!/mnt/d/software/python/python.exe -B

import re

input_file = open('day_14_input.txt', 'r')
input_data = [line.strip() for line in input_file.readlines()]

# Part One

mem_reg = {}
for line in input_data:
    if line.startswith('mask'):
        mask = line[-36:]
        and_mask = int(''.join([bit if bit == '0' else '1' for bit in mask]), 2)
        or_mask = int(''.join([bit if bit == '1' else '0' for bit in mask]), 2)
    elif line.startswith('mem'):
        id, value = re.findall(r'mem\[(\d+)\] = (\d+)', line)[0]
        mem_reg[id] = int(value) & and_mask | or_mask

total_value = sum(mem_reg.values())
print(total_value)

# Part Two

from itertools import chain, combinations

def powerset(arr):
    return chain.from_iterable(combinations(arr, r) for r in range(len(arr) + 1))

mem_reg = {}
for line in input_data:
    if line.startswith('mask'):
        mask = line[-36:]
        and_mask = int(''.join(['0' if bit == 'X' else '1' for bit in mask]), 2)
        or_mask = int(''.join([bit if bit == '1' else '0' for bit in mask]), 2)
        floating = [2**i for i, bit in enumerate(mask[::-1]) if bit == 'X']
    elif line.startswith('mem'):
        id, value = list(map(int, re.findall(r'mem\[(\d+)\] = (\d+)', line)[0]))
        for offset in map(sum, powerset(floating)):
            mem_reg[str(id & and_mask | or_mask + offset)] = value

total_value = sum(mem_reg.values())
print(total_value)
