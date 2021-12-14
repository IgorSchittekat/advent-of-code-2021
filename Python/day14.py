from aocd import get_data
from utils import *
from collections import Counter

data = get_data(year=2021, day=14)


def get_polymer_count(steps):
    polymer = data.splitlines()[0]
    mapping = dict()
    for key, val in splitlines(data, ' -> ')[2:]:
        mapping[key] = val
    count = Counter()
    total_count = Counter(polymer)
    for i in range(1, len(polymer)):
        count[f'{polymer[i - 1]}{polymer[i]}'] += 1
    for step in range(steps):
        new_count = Counter()
        for key, val in count.items():
            middle = mapping[key]
            new_count[f'{key[0]}{middle}'] += val
            new_count[f'{middle}{key[1]}'] += val
            total_count[middle] += val
        count = new_count
    counts = [v for k, v in sorted(total_count.items(), key=lambda item: item[1])]
    return counts[-1] - counts[0]


def part1():
    return get_polymer_count(10)


def part2():
    return get_polymer_count(40)


if __name__ == '__main__':
    _ = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    print(part1())
    print(part2())
