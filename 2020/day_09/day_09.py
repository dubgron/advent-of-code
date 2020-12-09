#!/mnt/d/software/python/python.exe -B

input_file = open('day_09_input.txt', 'r')
input_data = list(map(int, input_file.readlines()))
input_size = len(input_data)

# Part One

def is_summable_2(x, nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return True
    return False

for curr in range(25, input_size):
    x = input_data[curr]
    if not is_summable_2(x, input_data[curr - 25: curr]):
        break

print(x)

# Part Two

queue = []

for num in input_data:
    if num > x: continue
    queue.append(num)
    while sum(queue) > x:
        queue = queue[1:]
    if sum(queue) == x:
        break

print(min(queue) + max(queue))
