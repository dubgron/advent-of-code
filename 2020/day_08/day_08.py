#!/mnt/d/software/python/python.exe -B

input_file = open('day_08_input.txt', 'r')
input_data = input_file.readlines()
input_size = len(input_data)

def proceed(instructions):
    acc = 0
    line = 0
    visited = []

    while(line < len(instructions) and line not in visited):
        visited.append(line)
        (operation, value) = instructions[line]

        if operation == 'jmp':
            line += value
        elif operation == 'acc':
            acc += value
            line += 1
        elif operation == 'nop':
            line += 1

    return (acc, line)

instructions = list(map(lambda line: [line[0], int(line[1])], [line.split() for line in input_data]))

# Part One

acc = proceed(instructions)[0]
print(acc)

# Part Two

swap = { 'jmp': 'nop', 'nop': 'jmp' }

for i in instructions:
    if i[0] == 'acc': continue

    i[0] = swap[i[0]]
    (acc, line) = proceed(instructions)
    i[0] = swap[i[0]]

    if line == input_size: break

print(acc)
