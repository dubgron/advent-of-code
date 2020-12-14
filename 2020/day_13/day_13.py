#!/mnt/d/software/python/python.exe -B

import math

input_file = open('day_13_input.txt', 'r')
input_data = [line.strip() for line in input_file.readlines()]

# Part One

timestamp = int(input_data[0])
buses = [int(x) for x in input_data[1].split(',') if x != 'x']

score = []
for bus in buses:
    score.append((bus - timestamp % bus, bus))

best_score = math.prod(sorted(score)[0])
print(best_score)

# Part Two

def egcd(a, b):
    if a == 0:
        return (0, 1)
    else:
        x, y = egcd(b % a, a)
        return (y - (b // a) * x, x)

buses = [(int(x), i % int(x)) for i, x in enumerate(input_data[1].split(',')) if x != 'x']

n = [bus for bus, delay in buses]
y = [(bus - delay) % bus for bus, delay in buses]

n_prod = math.prod(n)
M = [int(n_prod / n_i) for n_i in n]

timestamp = sum([y_i * m_i * egcd(n_i, m_i)[1] for y_i, n_i, m_i in zip(y, n, M)]) % n_prod
print(timestamp)
