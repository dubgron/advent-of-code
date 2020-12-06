#!/mnt/d/software/python/python.exe -B

input_file = open('day_06_input.txt', 'r')
input_data = input_file.readlines()

# Part One

total = 0
ans = set()

for line in input_data + ['\n']:
    line = line.strip()
    if line == '':
        total += len(ans)
        ans = set()
    else:
        for l in line: ans.add(l)

print(total)

letters = list(map(chr, range(ord('a'), ord('z') + 1)))

total = 0
ans = set(letters)

for line in input_data + ['\n']:
    line = line.strip()
    if line == '':
        total += len(ans)
        ans = set(letters)
    else:
        ans &= set(line)

print(total)
