from aocd import get_data
from utils import *

data = get_data(year=2021, day=18)


# def get_last_number(stack):
#     for elem in reversed(stack):
#         if isinstance(elem, int):
#             return elem
#         elif isinstance(elem, list):
#             return get_last_number(elem)


# def explode(pair, stack, depth=1, idx=0):
#     exploded = False
#     stack.append((pair, depth))
#     if depth > 4:
#         exploded = True
#         numb_id = get_last_number(stack[:-1][0])
#         print(ints(str(stack[0])))
#         print(idx)
#
#     else:
#         if isinstance(pair[0], int):
#             idx += 1
#         if isinstance(pair[0], list):
#             exploded, idx = explode(pair[0], stack, depth + 1, idx)
#             pair, depth = stack.pop()
#         if isinstance(pair[1], int):
#             idx += 1
#         if isinstance(pair[1], list):
#             exploded, idx = explode(pair[1], stack, depth + 1, idx)
#             pair, depth = stack.pop()
#
#
#
#     return exploded, idx

def get_nr_before(addition, idx):
    numbers = ints(addition[:idx])
    if numbers:
        last_num = str(numbers[-1])
        return addition[:idx].rfind(last_num), len(last_num)
    return None, None


def get_nrs_after(addition, idx):
    numbers = ints(addition[idx:])
    num_1 = numbers[0]
    num_2 = numbers[1]
    if len(numbers) > 2:
        num_3 = str(numbers[2])
        return num_1, num_2, addition[idx + len(str(num_1)) + len(str(num_2)) + 2:].find(num_3), len(num_3)
    return num_1, num_2, None, None


def explode(addition):
    stack = list()
    for i, char in enumerate(addition):
        if char == '[':
            stack.append(i)
        if char == ']':
            stack.pop()
        if len(stack) > 4:
            num_1, num_2, start, end = get_nrs_after(addition, i)
            start_2, end_2 = get_nr_before(addition, i)
            if start is not None:
                start = i + start + len(str(num_1)) + len(str(num_2)) + 2
                end = start + end
                addition = f"{addition[:start]}{int(addition[start:end]) + num_2}{addition[end:]}"
            addition = f"{addition[:i]}0{addition[i + len(str(num_1)) + len(str(num_2)) + 3:]}"
            if start_2 is not None:
                addition = f"{addition[:start_2]}{int(addition[start_2:start_2 + end_2]) + num_1}{addition[start_2 + end_2:]}"
            return addition, True
    return addition, False


def split(addition):
    numbers = ints(addition)
    for number in numbers:
        if number >= 10:
            idx = addition.find(str(number))
            num_1 = str(math.floor(number / 2))
            num_2 = str(math.ceil(number / 2))
            addition = f"{addition[:idx]}[{num_1},{num_2}]{addition[idx + len(str(number)):]}"
            return addition, True
    return addition, False


def add(first, second):
    addition = f"[{first},{second}]"
    change = True
    while change:
        addition, change = explode(addition)
        if change:
            continue
        addition, change = split(addition)

    return addition


def str_to_list(s):
    l = list()
    stack = list()
    for char in s[1:-1]:
        if char == '[':
            stack.append(l)
            l = list()
        elif char == ']':
            stack[-1].append(l)
            l = stack.pop()
        elif char != ',':
            l.append(int(char))
    return l


def magnitude(pair):
    if isinstance(pair[0], int):
        first = 3 * pair[0]
    else:
        first = 3 * magnitude(pair[0])
    if isinstance(pair[1], int):
        second = 2 * pair[1]
    else:
        second = 2 * magnitude(pair[1])
    return first + second


def part1():
    total = data.splitlines()[0]
    for line in data.splitlines()[1:]:
        total = add(total, line)
    return magnitude(str_to_list(total))


def part2():
    largest = 0
    for i, num_1 in enumerate(data.splitlines()):
        for j, num_2 in enumerate(data.splitlines()):
            if i != j:
                total = add(num_1, num_2)
                largest = max(largest, magnitude(str_to_list(total)))
    return largest


if __name__ == '__main__':
    _ = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    print(part1())
    print(part2())
