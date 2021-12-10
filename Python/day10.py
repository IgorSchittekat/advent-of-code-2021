from aocd import get_data
from utils import *

data = get_data(year=2021, day=10)


def part1():
    total = 0
    for line in data.splitlines():
        stack = []
        match = {'(': ')', '[': ']', '{':'}', '<':'>'}
        points = {')': 3, ']': 57, '}': 1197, '>': 25137}
        for char in line:
            if char in match.keys():
                stack.append(char)
            elif match[stack.pop()] != char:
                total += points[char]
                break
    return total


def part2():
    scores = []
    for line in data.splitlines():
        stack = []
        match = {'(': ')', '[': ']', '{': '}', '<': '>'}
        points = {')': 1, ']': 2, '}': 3, '>': 4}
        score = 0
        for char in line:
            if char in match.keys():
                stack.append(char)
            elif match[stack.pop()] != char:
                break
        else:
            while stack:
                score = score * 5 + points[match[stack.pop()]]
            scores.append(score)
    return sorted(scores)[int(len(scores) / 2)]


if __name__ == '__main__':
    _ = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    print(part1())
    print(part2())
