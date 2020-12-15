#!/mnt/d/software/python/python.exe -B

input_file = open('day_15_input.txt', 'r')
input_data = list(map(int, input_file.read().split(',')))

def play(start, steps):
    age = { num: [i, None] for i, num in enumerate(start) }
    last = start[-1]

    for turn in range(len(start), steps):
        if age[last][1] is None: last = 0
        else: last = age[last][0] - age[last][1]

        if last in age:
            age[last][1] = age[last][0]
            age[last][0] = turn
        else:
            age[last] = [turn, None]

    return last

# Part One

last = play(input_data, 2020)
print(last)

# Part Two

last = play(input_data, 30000000)
print(last)
