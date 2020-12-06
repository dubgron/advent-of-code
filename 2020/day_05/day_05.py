#!/mnt/d/software/python/python.exe -B

input_file = open('day_05_input.txt', 'r')
input_data = input_file.readlines()

MAX_ROW = 128
MAX_COL = 8

def row(line):
    row = [0, MAX_ROW - 1]
    for c in line[:-3]:
        if c == 'F': row[1] = int((row[0] + row[1] - 1) / 2)
        if c == 'B': row[0] = int((row[0] + row[1] + 1) / 2)
    return row[0]

def col(line):
    col = [0, MAX_COL - 1]
    for c in line[-3:]:
        if c == 'L': col[1] = int((col[0] + col[1] - 1) / 2)
        if c == 'R': col[0] = int((col[0] + col[1] + 1) / 2)
    return col[0]

def id(line):
    return 8 * row(line) + col(line)

# Part One

ids = []

for line in input_data:
    line = line.strip()
    ids.append(id(line))

score = sorted(ids)[-1]
print(score)

# Part Two

seats = range(MAX_ROW * MAX_COL)
free_seats = [seat for seat in seats if seat not in ids]

for i in range(1, len(free_seats)):
    seat = free_seats[i]
    if free_seats[i - 1] != seat - 1 and free_seats[i + 1] != seat + 1:
        print(seat)
