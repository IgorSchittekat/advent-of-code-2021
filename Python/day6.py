from collections import defaultdict, Counter


def read_input():
    with open('input6.txt', 'r') as file:
        line = file.read()
        return [int(number) for number in line.rstrip().split(',')]


def growth(days):
    line = read_input()
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
