from collections import defaultdict, Counter
from aocd import get_data
from utils import *

data = get_data(year=2021, day=6)


def growth(days):
    line = ints(data)
    count = dict(Counter(line))
    for day in range(days):
        new_count = defaultdict(int)
        for i in range(9):
            if i == 0:
                new_count[6] += count.get(i, 0)
                new_count[8] += count.get(i, 0)
            else:
                new_count[i - 1] += count.get(i, 0)
        count = dict(new_count)
    return sum(count.values())


def part1():
    return growth(80)


def part2():
    return growth(256)


if __name__ == '__main__':
    print(part1())
    print(part2())
