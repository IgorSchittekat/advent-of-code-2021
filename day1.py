
def read_input():
    with open('input1.txt', 'r') as file:
        lines = file.readlines()
        return [int(line.rstrip()) for line in lines]


def day1_1():
    lines = read_input()
    prev = lines[0]
    counter = 0
    for number in lines[1:]:
        if number > prev:
            counter += 1
        prev = number
    return counter


def day1_2():
    lines = read_input()
    prev = sum(lines[:3])
    counter = 0
    for i in range(1, len(lines) - 2):
        number = sum(lines[i:i+3])
        if number > prev:
            counter += 1
        prev = number
    return counter
