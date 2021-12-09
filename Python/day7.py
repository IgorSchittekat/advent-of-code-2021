import math
from aocd import get_data
from utils import *

data = get_data(year=2021, day=7)


def part1():
    positions = ints(data)
    smallest = math.inf
    for i in range(max(positions)):
        total = 0
        for pos in positions:
            total += abs(i - pos)
        smallest = min(smallest, total)
    return smallest


def part2():
    positions = ints(data)
    val = [0]
    for i in range(1, max(positions) + 1):
        val.append(val[i - 1] + i)
    smallest = math.inf
    for i in range(max(positions)):
        total = 0
        for pos in positions:
            total += val[abs(i - pos)]
        smallest = min(smallest, total)
    return smallest


if __name__ == '__main__':
    print(part1())
    print(part2())
