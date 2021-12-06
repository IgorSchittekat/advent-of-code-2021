import numpy as np


def read_input():
    with open('input3.txt', 'r') as file:
        lines = file.readlines()
        lines = [[char for char in line.rstrip()] for line in lines]
        return np.array(lines)


def get_zeros_and_ones(arr):
    n_row, n_col = arr.shape
    zeros = np.zeros(n_col)
    ones = np.zeros(n_col)
    for row in arr:
        for i, col in enumerate(row):
            if col == '0':
                zeros[i] += 1
            if col == '1':
                ones[i] += 1
    return zeros, ones


def part1():
    lines = read_input()
    n_row, n_col = lines.shape
    zeros, ones = get_zeros_and_ones(lines)
    gamma = np.zeros(n_col)
    epsilon = np.zeros(n_col)
    for i in range(n_col):
        if zeros[i] > ones[i]:
            epsilon[i] = 1
        else:
            gamma[i] = 1
    gamma = gamma.dot(1 << np.arange(gamma.shape[-1] - 1, -1, -1))
    epsilon = epsilon.dot(1 << np.arange(epsilon.shape[-1] - 1, -1, -1))
    return int(gamma * epsilon)


def filter(arr, idx, number):
    new_arr = []
    for line in arr:
        if line[idx] == number:
            new_arr.append(line)
    return np.array(new_arr)


def oxygen():
    lines = read_input()
    n_row, n_col = lines.shape
    for i in range(n_col):
        if len(lines) == 1:
            break
        zeros, ones = get_zeros_and_ones(lines)
        if zeros[i] > ones[i]:
            lines = filter(lines, i, '0')
        else:
            lines = filter(lines, i, '1')
    lines = lines.astype(np.int)
    return lines.dot(1 << np.arange(lines.shape[-1] - 1, -1, -1))[0]


def co2():
    lines = read_input()
    n_row, n_col = lines.shape
    for i in range(n_col):
        if len(lines) == 1:
            break
        zeros, ones = get_zeros_and_ones(lines)
        if zeros[i] <= ones[i]:
            lines = filter(lines, i, '0')
        else:
            lines = filter(lines, i, '1')
    lines = lines.astype(np.int)
    return lines.dot(1 << np.arange(lines.shape[-1] - 1, -1, -1))[0]


def part2():
    return oxygen() * co2()


if __name__ == '__main__':
    print(part1())
    print(part2())
