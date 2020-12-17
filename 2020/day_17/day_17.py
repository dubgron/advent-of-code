#!/mnt/d/software/python/python.exe -B

input_file = open('day_17_input.txt', 'r')
input_data = [list(line.strip()) for line in input_file]

def vec_add(v1, v2):
    return tuple(x + y for x, y in zip(v1, v2))

def neighbors_count(cube, board, offset):
    return sum([vec_add(cube, cube_off) in board for cube_off in offset])

def simulate(board, cycles, get_boundries, offset):
    for i in range(cycles):
        new_board = board.copy()
        for cube in get_boundries(board):
            neighbors = neighbors_count(cube, board, offset)
            if cube in board and neighbors not in (2, 3):
                new_board.remove(cube)
            elif cube not in board and neighbors == 3:
                new_board.add(cube)
        board = new_board

    return board

board_3d = set()
board_4d = set()
for y in range(len(input_data)):
    for x in range(len(input_data[y])):
        if input_data[y][x] == '#':
            board_3d.add((x, y, 0))
            board_4d.add((x, y, 0, 0))

offset_3d = []
offset_4d = []
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        for z in (-1, 0, 1):
            for w in (-1, 0, 1):
                offset_4d.append((x, y, z, w))
            offset_3d.append((x, y, z))
offset_3d.remove((0, 0, 0))
offset_4d.remove((0, 0, 0, 0))

# Part One

def get_boundries_3d(board_3d):
    mins = [min(board_3d, key=lambda x: x[i])[i] - 1 for i in range(3)]
    maxs = [max(board_3d, key=lambda x: x[i])[i] + 1 for i in range(3)]
    for x in range(mins[0], maxs[0] + 1):
        for y in range(mins[1], maxs[1] + 1):
            for z in range(mins[2], maxs[2] + 1):
                yield (x, y, z)

board_3d = simulate(board_3d, 6, get_boundries_3d, offset_3d)
active = len(board_3d)
print(active)

# Part Two

def get_boundries_4d(board_4d):
    mins = [min(board_4d, key=lambda x: x[i])[i] - 1 for i in range(4)]
    maxs = [max(board_4d, key=lambda x: x[i])[i] + 1 for i in range(4)]
    for x in range(mins[0], maxs[0] + 1):
        for y in range(mins[1], maxs[1] + 1):
            for z in range(mins[2], maxs[2] + 1):
                for w in range(mins[3], maxs[3] + 1):
                    yield (x, y, z, w)

board_4d = simulate(board_4d, 6, get_boundries_4d, offset_4d)
active = len(board_4d)
print(active)
