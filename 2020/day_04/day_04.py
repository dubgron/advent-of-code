#!/mnt/d/software/python/python.exe -B

import re

input_file = open('day_04_input.txt', 'r')
input_data = input_file.readlines()

# Part One

valids = 0

recquire = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
fields = []

for line in input_data:
    if line == '\n':
        valids += (sorted(recquire) == sorted(fields))
        fields = []
    else:
        fields += [x.split(':')[0] for x in line.split(' ') if x.split(':')[0] != 'cid']

valids += (sorted(recquire) == sorted(fields))

print(valids)

# Part Two

valids = 0
fields = []
values = []

def validate():
    valid = True
    for field, value in zip(fields, values):
        if field == 'byr' and (int(value) < 1920 or int(value) > 2002): valid = False
        if field == 'iyr' and (int(value) < 2010 or int(value) > 2020): valid = False
        if field == 'eyr' and (int(value) < 2020 or int(value) > 2030): valid = False
        if field == 'hgt' and value[-2:] not in ('cm', 'in'): valid = False
        if field == 'hgt' and value.endswith('cm') and (int(value[:-2]) < 150 or int(value[:-2]) > 193): valid = False
        if field == 'hgt' and value.endswith('in') and (int(value[:-2]) < 59 or int(value[:-2]) > 76): valid = False
        if field == 'hcl' and not re.match(r'^#[0-9a-f]{6}$', value): valid = False
        if field == 'ecl' and value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): valid = False
        if field == 'pid' and len(value) != 9: valid = False

    return (sorted(recquire) == sorted(fields) and valid)

for line in input_data:
    if line == '\n':
        valids += validate()
        fields = []
        values = []
    else:
        data = [x.split(':') for x in line.split(' ') if x.split(':')[0] != 'cid']
        fields += [x[0].strip() for x in data]
        values += [x[1].strip() for x in data]

valids += validate()

print(valids)
