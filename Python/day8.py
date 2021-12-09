from aocd import get_data
from utils import *

data = get_data(year=2021, day=8)


def part1():
    outputs = [line[-4:] for line in splitlines(data, ' ')]
    counter = 0
    for output in outputs:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                counter += 1
    return counter


def part2():
    lines = splitlines(data, ' ')
    total = 0
    for line in lines:
        mapping = dict()
        numbers = sorted(line[:10], key=len)
        mapping[1] = set(numbers[0])
        mapping[7] = set(numbers[1])
        mapping[4] = set(numbers[2])
        mapping[8] = set(numbers[9])

        for number in numbers[6:9]:
            number = set(number)
            if mapping[4].issubset(number):
                mapping[9] = number
            elif mapping[1].issubset(number):
                mapping[0] = number
            else:
                mapping[6] = number

        for number in numbers[3:6]:
            number = set(number)
            if mapping[1].issubset(number):
                mapping[3] = number
            elif number.issubset(mapping[6]):
                mapping[5] = number
            else:
                mapping[2] = number

        output = ""
        for number in line[-4:]:
            number = set(number)
            output += str(list(mapping.keys())[list(mapping.values()).index(number)])
        total += int(output)
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())
