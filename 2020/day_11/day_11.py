#!/mnt/d/software/python/python.exe -B

input_file = open('day_11_input.txt', 'r')
input_data = [line.strip() for line in input_file.readlines()]

empty = 'L'
floor = '.'
occupied = '#'

width = len(input_data[0]) + 2
height = len(input_data) + 2
def create_layout():
    return list(''.join(['.' * width] + ['.{}.'.format(line) for line in input_data] + ['.' * width]))

# Part One

def neighbors(seat, layout):
    n = 0
    n += (layout[seat - 1] == occupied)
    n += (layout[seat + 1] == occupied)
    n += (layout[seat - width] == occupied)
    n += (layout[seat - width - 1] == occupied)
    n += (layout[seat - width + 1] == occupied)
    n += (layout[seat + width] == occupied)
    n += (layout[seat + width - 1] == occupied)
    n += (layout[seat + width + 1] == occupied)
    return n

layout = create_layout()
layout_cpy = []
while layout != layout_cpy:
    layout_cpy = layout.copy()
    for i in range(len(layout_cpy)):
        seat = layout_cpy[i]
        if seat is empty and neighbors(i, layout_cpy) == 0:
            layout[i] = occupied
        elif seat is occupied and neighbors(i, layout_cpy) >= 4:
            layout[i] = empty

occupied_count = sum([1 for seat in layout if seat == occupied])
print(occupied_count)

# Part Two

def neighbors_2(seat, layout):
    n = 0

    def trace_neighbor(start, stop, step):
        for i in range(start, stop, step):
            seat = layout[i]
            if seat is empty: return 0
            elif seat is occupied: return 1
        return 0

    x = seat % width
    y = int(seat / width)

    n += trace_neighbor(seat - width, x - 1, -width)
    n += trace_neighbor(seat + width, len(layout) - width + x + 1, width)
    n += trace_neighbor(seat - 1, seat - x - 1, -1)
    n += trace_neighbor(seat + 1, seat + width - x, 1)
    n += trace_neighbor(seat - width - 1, seat - min(x, y) * (width + 1) - 1, -width - 1)
    n += trace_neighbor(seat + width + 1, seat + min(width - x, height - y) * width, width + 1)
    n += trace_neighbor(seat - width + 1, seat - min(width - x - 1, y) * (width - 1) - 1, -width + 1)
    n += trace_neighbor(seat + width - 1, seat + min(x, height - y - 1) * width, width - 1)
    return n

layout = create_layout()
layout_cpy = []
while layout != layout_cpy:
    layout_cpy = layout.copy()
    for i in range(len(layout_cpy)):
        seat = layout_cpy[i]
        if seat is empty and neighbors_2(i, layout_cpy) == 0:
            layout[i] = occupied
        elif seat is occupied and neighbors_2(i, layout_cpy) >= 5:
            layout[i] = empty

occupied_count = sum([1 for seat in layout if seat == occupied])
print(occupied_count)
