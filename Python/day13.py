import numpy
import numpy as np
from aocd import get_data
from utils import *

data = get_data(year=2021, day=13)


def create_matrix():
    points = []
    foldlines = []
    for line in splitlines(data, ','):
        if len(line) == 2:
            points.append(tuple([int(num) for num in line]))
        elif line[0] != '':
            foldlines.append(line[0].split('='))
    max_x = max([point[0] for point in points])
    max_y = max([point[1] for point in points])
    matrix = np.zeros((max_y + 1, max_x + 1), dtype=int)
    for x, y in points:
        matrix[y][x] = 1
    return foldlines, matrix


def fold(matrix, foldline):
    if foldline[0] == 'fold along x':
        flipped = np.fliplr(matrix)
        x = int(foldline[1])
        new_matrix = np.zeros((matrix.shape[0], x), dtype=int)
    else:
        flipped = np.flipud(matrix)
        y = int(foldline[1])
        new_matrix = np.zeros((y, matrix.shape[1]), dtype=int)
    for row in range(new_matrix.shape[0]):
        for col in range(new_matrix.shape[1]):
            if matrix[row][col] or flipped[row][col]:
                new_matrix[row][col] = 1
    return new_matrix


def part1():
    foldlines, matrix = create_matrix()
    matrix = fold(matrix, foldlines[0])
    return np.count_nonzero(matrix)


def part2():
    foldlines, matrix = create_matrix()
    for foldline in foldlines:
        matrix = fold(matrix, foldline)
    matrix = matrix.astype(str)
    matrix[matrix == '0'] = ' '
    matrix[matrix == '1'] = '#'
    return matrix


if __name__ == '__main__':
    _ = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    print(part1())
    print_grid(part2())
