import numpy as np
from aocd import get_data
from utils import *
from collections import defaultdict

data = get_data(year=2021, day=15)


def grid_to_graph(grid):
    graph = defaultdict(lambda: dict())
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            for r, c in get_neighbors_coords(grid, i, j, GRID_DELTA):
                graph[(r, c)][(i, j)] = num
    return graph


def part1():
    grid = np.array([[int(char) for char in row] for row in data.splitlines()])
    graph = grid_to_graph(grid)
    dj = dijkstra(graph, (0, 0))
    return dj[(grid.shape[0] - 1, grid.shape[1] - 1)]


def part2():
    grid = np.array([[int(char) for char in row] for row in data.splitlines()])
    big_grid = np.zeros((grid.shape[0] * 5, grid.shape[1] * 5), dtype=int)
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            for x in range(5):
                for y in range(5):
                    new_num = (num + x + y) % 9
                    if new_num == 0:
                        new_num = 9
                    big_grid[grid.shape[0] * x + i][grid.shape[1] * y + j] = new_num
    graph = grid_to_graph(big_grid)
    dj = dijkstra(graph, (0, 0))
    return dj[(big_grid.shape[0] - 1, big_grid.shape[1] - 1)]


if __name__ == '__main__':
    _ = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    print(part1())
    print(part2())
