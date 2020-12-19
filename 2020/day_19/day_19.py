#!/mnt/d/software/python/python.exe -B

import re

input_file = open('day_19_input.txt', 'r')
input_data = input_file.read()

separator = ' | '

def expand_rules(start):
    start = int(start)
    rule = rules[start]
    if re.match(r'^[^A-z]+$', rule):
        expanded = [tuple(map(expand_rules, r.split(' '))) for r in rule.split(separator)]
        rules[start] = '(' + '|'.join([''.join(r) for r in expanded]) + ')'

    return rules[start]

# Part One

rules = { int(line[0]): line[1].strip('"') for line in re.findall(r'^(\d+): (.*)$', input_data, re.MULTILINE) }

rule = '^' + expand_rules(0) + '$'
total = sum([1 for line in input_data.split('\n') if re.match(rule, line)])
print(total)

# Part Two

rules = { int(line[0]): line[1].strip('"') for line in re.findall(r'^(\d+): (.*)$', input_data, re.MULTILINE) }

depth = 6
for i in range(2, depth):
    # rules[8] = '42 | 42 8'
    rules[8] += separator + ' '.join(['42'] * i)
    # rules[11] = '42 31 | 42 11 31'
    rules[11] += separator + ' '.join(['42'] * i + ['31'] * i)

rule = '^' + expand_rules(0) + '$'
total = sum([1 for line in input_data.split('\n') if re.match(rule, line)])
print(total)
