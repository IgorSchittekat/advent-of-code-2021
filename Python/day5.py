import numpy as np
from aocd import get_data
from utils import *

data = get_data(year=2021, day=5)


class Field:
    def __init__(self):
        self.grid = np.zeros((1000, 1000), dtype=int)

    def add_line(self, x1, y1, x2, y2):
        if x1 == x2:
            dir = 1
            if y1 > y2:
                dir = -1
            for y in range(y1, y2 + dir, dir):
                self.grid[x1][y] += 1
        elif y1 == y2:
            dir = 1
            if x1 > x2:
                dir = -1
            for x in range(x1, x2 + dir, dir):
                self.grid[x][y1] += 1
        else:
            xdir = ydir = 1
            if x1 > x2:
                xdir = -1
            if y1 > y2:
                ydir = -1
            for i in range(abs(x1 - x2) + 1):
                self.grid[x1 + i * xdir][y1 + i * ydir] += 1

    def count_twos(self):
        counter = 0
        for row in self.grid:
            for col in row:
                if col >= 2:
                    counter += 1
        return counter


def parse_line(line):
    x1, y1 = line[0].split(',')
    x2, y2 = line[1].split(',')
    return int(x1), int(y1), int(x2), int(y2)


def part1():
    lines = splitlines(data, ' -> ')
    field = Field()
    for line in lines:
        x1, y1, x2, y2 = parse_line(line)
        if x1 == x2 or y1 == y2:
            field.add_line(x1, y1, x2, y2)
    return field.count_twos()


def part2():
    lines = splitlines(data, ' -> ')
    field = Field()
    for line in lines:
        x1, y1, x2, y2 = parse_line(line)
        field.add_line(x1, y1, x2, y2)
    return field.count_twos()


if __name__ == '__main__':
    print(part1())
    print(part2())
