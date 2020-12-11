#!/mnt/d/software/python/python.exe -B

input_file = open('day_10_input.txt', 'r')
input_data = sorted(list(map(int, input_file.readlines())))

outlet_joltage = 0
device_joltage = max(input_data) + 3

# Part One

diff = { 1: 0, 2: 0, 3: 0 }
curr_joltage = outlet_joltage

for joltage in input_data + [device_joltage]:
    diff[joltage - curr_joltage] += 1
    curr_joltage = joltage

print(diff[1] * diff[3])

# Part Two

combinations = 1
variations = { 0: 1, 1: 1, 2: 1, 3: 2, 4: 4, 5: 7 }

prev = 0
streak_count = 1
for joltage in input_data + [device_joltage]:
    if prev + 1 == joltage:
        streak_count += 1
    else:
        combinations *= variations[streak_count]
        streak_count = 1
    prev = joltage

print(combinations)
