from aocd import get_data
from utils import *

data = get_data(year=2021, day=1)


def part1():
    numbers = ints(data)
    prev = numbers[0]
    counter = 0
    for number in numbers[1:]:
        if number > prev:
            counter += 1
        prev = number
    return counter


def part2():
    numbers = ints(data)
    prev = sum(numbers[:3])
    counter = 0
    for i in range(1, len(numbers) - 2):
        number = sum(numbers[i:i+3])
        if number > prev:
            counter += 1
        prev = number
    return counter


if __name__ == '__main__':
    print(part1())
    print(part2())
