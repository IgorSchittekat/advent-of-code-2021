import math

from aocd import get_data
from utils import *

data = get_data(year=2021, day=17)


def hit_target(v_x, v_y):
    min_x, max_x, min_y, max_y = ints(data)
    probe = (0, 0)
    highest = 0
    while probe[0] <= max_x and probe[1] >= min_y:
        probe = (probe[0] + v_x, probe[1] + v_y)
        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x += 1
        v_y -= 1
        highest = max(highest, probe[1])
        if min_x <= probe[0] <= max_x and min_y <= probe[1] <= max_y:
            return True, highest
    return False, highest


def part1():
    min_x, max_x, min_y, max_y = ints(data)
    all_high = 0
    for x in range(int(math.sqrt(min_x)) - 1, max_x + 1):
        for y in range(min_y, - min_y):
            hit, highest = hit_target(x, y)
            if hit:
                all_high = max(all_high, highest)
    return all_high


def part2():
    min_x, max_x, min_y, max_y = ints(data)
    total = 0
    for x in range(int(math.sqrt(min_x)) - 1, max_x + 1):
        for y in range(min_y, - min_y):
            hit, highest = hit_target(x, y)
            if hit:
                total += 1
    return total


if __name__ == '__main__':
    _ = "target area: x=20..30, y=-10..-5"
    print(part1())
    print(part2())
