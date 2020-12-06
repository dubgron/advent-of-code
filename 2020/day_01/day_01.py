#!/mnt/d/software/python/python.exe -B

input_file = open('day_01_input.txt', 'r')
input_data = [int(x) for x in input_file.readlines()]
input_size = len(input_data)

# Part One

for i in range(input_size):
    for j in range(i, input_size):
        if input_data[i] + input_data[j] == 2020:
            print(input_data[i] * input_data[j])
            break

# Part Two

for i in range(input_size):
    for j in range(i, input_size):
        for k in range(j, input_size):
            if input_data[i] + input_data[j] + input_data[k] == 2020:
                print(input_data[i] * input_data[j] * input_data[k])
                break
