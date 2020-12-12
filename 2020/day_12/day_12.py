#!/mnt/d/software/python/python.exe -B

import math

input_file = open('day_12_input.txt', 'r')
input_data = [line.strip() for line in input_file.readlines()]

north = 'N'
east = 'E'
south = 'S'
west = 'W'
left = 'L'
right = 'R'
forward = 'F'

dir_north = 0
dir_east = 1
dir_south = 2
dir_west = 3

instructions = list(map(lambda x: (x[0], int(x[1:])), input_data))

class vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def forward(self, facing, step):
        if facing is dir_north: self.y += step
        elif facing is dir_east: self.x += step
        elif facing is dir_south: self.y -= step
        elif facing is dir_west: self.x -= step

    def rotate(self, angle):
        if angle == 90:
            self.__init__(-self.y, self.x)
        elif angle == 180:
            self.__init__(-self.x, -self.y)
        elif angle == 270:
            self.__init__(self.y, -self.x)

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __mul__(self, value):
        return vec2(self.x * value, self.y * value)

# Part One

facing = dir_east
position = vec2()

for action, value in instructions:
    if action is north: position.y += value
    elif action is east: position.x += value
    elif action is south: position.y -= value
    elif action is west: position.x -= value
    elif action is left: facing = int(facing - value / 90) % 4
    elif action is right: facing = int(facing + value / 90) % 4
    elif action is forward: position.forward(facing, value)

print(position.manhattan())

# Part Two
position = vec2()
waypoint = vec2(10, 1)

for action, value in instructions:
    if action is north: waypoint.y += value
    elif action is east: waypoint.x += value
    elif action is south: waypoint.y -= value
    elif action is west: waypoint.x -= value
    elif action is left: waypoint.rotate(value)
    elif action is right: waypoint.rotate(360 - value)
    elif action is forward: position += waypoint * value

print(position.manhattan())
