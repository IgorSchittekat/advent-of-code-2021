import math


def read_input():
    with open('input7.txt', 'r') as file:
        line = file.read()
        return [int(number) for number in line.rstrip().split(',')]


def part1():
    positions = read_input()
    smallest = math.inf
    for i in range(max(positions)):
        total = 0
        for pos in positions:
            total += abs(i - pos)
        smallest = min(smallest, total)
    return smallest


def part2():
    positions = read_input()
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
