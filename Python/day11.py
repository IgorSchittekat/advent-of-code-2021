from aocd import get_data
from utils import *
import numpy as np

data = get_data(year=2021, day=11)


def flash_neighbors(grid, i, j, flashed):
    for row, col in get_neighbors_coords(grid, i, j, OCT_DELTA):
        grid[row][col] += 1
        if grid[row][col] > 9 and not flashed[row][col]:
            flashed[row][col] = True
            flash_neighbors(grid, row, col, flashed)
    return flashed


def flash_all(grid):
    flashed = np.zeros((len(grid), len(grid[0])), dtype=int)
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num > 9 and not flashed[i][j]:
                flashed[i][j] = True
                flashed = flash_neighbors(grid, i, j, flashed)
    return flashed


def part1():
    grid = np.array([[int(number) for number in line] for line in data.splitlines()])
    total_flashes = 0
    for _ in range(100):
        grid += 1
        total_flashes += np.count_nonzero(flash_all(grid))
        grid[grid > 9] = 0
    return total_flashes


def part2():
    grid = np.array([[int(number) for number in line] for line in data.splitlines()])
    step = 0
    while True:
        step += 1
        grid += 1
        flashed = flash_all(grid)
        grid[grid > 9] = 0
        if flashed.all():
            break
    return step


if __name__ == '__main__':
    _ = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    print(part1())
    print(part2())
