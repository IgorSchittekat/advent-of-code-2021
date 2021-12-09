import numpy as np
from aocd import get_data
from utils import *

data = get_data(year=2021, day=9)


def read_input():
    return np.array([[int(char) for char in line] for line in data.splitlines()])


def find_lowpoint(i, j, lines):
    num = lines[i][j]
    if i > 0 and num >= lines[i - 1][j]:
        return False
    if i + 1 < len(lines) and num >= lines[i + 1][j]:
        return False
    if j > 0 and num >= lines[i][j - 1]:
        return False
    if j + 1 < len(lines[i]) and num >= lines[i][j + 1]:
        return False
    return True


def part1():
    lines = read_input()
    total = 0
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            if find_lowpoint(i, j, lines):
                total += num + 1
    return total


def get_basin_size(i, j, lines, visited, size):
    if (i, j) in visited or lines[i][j] == 9:
        return visited, size
    visited.append((i, j))
    size += 1
    if i > 0:
        visited, size = get_basin_size(i - 1, j, lines, visited, size)
    if i + 1 < len(lines):
        visited, size = get_basin_size(i + 1, j, lines, visited, size)
    if j > 0:
        visited, size = get_basin_size(i, j - 1, lines, visited, size)
    if j + 1 < len(lines[i]):
        visited, size = get_basin_size(i, j + 1, lines, visited, size)
    return visited, size


def part2():
    lines = read_input()
    basins = []
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            if find_lowpoint(i, j, lines):
                _, size = get_basin_size(i, j, lines, [], 0)
                basins.append(size)
    return np.prod(sorted(basins)[-3:])


if __name__ == '__main__':
    print(part1())
    print(part2())
