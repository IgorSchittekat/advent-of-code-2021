from aocd import get_data
from utils import *
from collections import defaultdict

data = get_data(year=2021, day=12)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_all_paths_until(self, current, end, visited, path, total, lower=None):
        if not current[0].isupper():
            visited[current] = True
            if lower == current:
                visited[current] = False
                lower = None
        path.append(current)

        if current == end:
            total.add(tuple(path))
        else:
            for i in self.graph[current]:
                if not visited[i]:
                    self.get_all_paths_until(i, end, visited, path, total, lower)

        path.pop()
        visited[current] = False

    def get_all_paths(self, start, end, twice):
        visited = defaultdict(lambda: False)

        path = []
        if twice:
            lowers = []
            for key in self.graph:
                if not key[0].isupper() and key not in ['start', 'end']:
                    lowers.append(key)
            paths = set()
            for lower in lowers:
                self.get_all_paths_until(start, end, visited, path, paths, lower)
            return paths
        else:
            paths = set()
            self.get_all_paths_until(start, end, visited, path, paths)
            return paths


def create_graph():
    graph = Graph()
    for line in splitlines(data, '-'):
        graph.add_edge(line[0], line[1])
        graph.add_edge(line[1], line[0])
    return graph


def part1():
    graph = create_graph()
    return len(graph.get_all_paths('start', 'end', False))


def part2():
    graph = create_graph()
    return len(graph.get_all_paths('start', 'end', True))


if __name__ == '__main__':
    _ = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    _ = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
    _ = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
    print(part1())
    print(part2())
