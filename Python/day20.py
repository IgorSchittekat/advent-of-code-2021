from aocd import get_data
from utils import *
import numpy as np

data = get_data(year=2021, day=20)

IMAGE_DELTA = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]


def enhance(steps):
    algorithm = data.splitlines()[0]
    image = np.array([['1' if char == '#' else '0' for char in line] for line in data.splitlines()[2:]])
    image = np.pad(image, pad_width=steps + 1, mode='constant', constant_values='0')
    for step in range(steps):
        new_image = np.zeros(image.shape, dtype=int).astype(str)
        for i, row in enumerate(image[1:-1]):
            for j, num in enumerate(row[1:-1]):
                coords = get_neighbors_coords(image, i + 1, j + 1, IMAGE_DELTA)
                binary = f""
                for x, y in coords:
                    binary += image[x][y]
                new_image[i + 1][j + 1] = '1' if algorithm[int(binary, 2)] == '#' else '0'
        new_image = new_image[1:new_image.shape[0] - 1, 1:new_image.shape[1] - 1]
        image = np.pad(new_image, pad_width=1, mode='constant', constant_values=new_image[0][0])
    return np.count_nonzero(image.astype(int))


def part1():
    return enhance(2)


def part2():
    return enhance(50)


if __name__ == '__main__':
    _ = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
    print(part1())
    print(part2())
