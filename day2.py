

def read_input():
    with open('input2.txt', 'r') as file:
        lines = file.readlines()
        return [line.rstrip().split(' ') for line in lines]


def day2_1():
    lines = read_input()
    depth = 0
    horizontal = 0
    for direction, amount in lines:
        amount = int(amount)
        if direction == 'forward':
            horizontal += amount
        elif direction == 'up':
            depth -= amount
        elif direction == 'down':
            depth += amount
    return depth * horizontal


def day2_2():
    lines = read_input()
    depth = 0
    horizontal = 0
    aim = 0
    for direction, amount in lines:
        amount = int(amount)
        if direction == 'forward':
            horizontal += amount
            depth += aim * amount
        elif direction == 'up':
            aim -= amount
        elif direction == 'down':
            aim += amount
    return depth * horizontal