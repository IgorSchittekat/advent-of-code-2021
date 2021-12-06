import numpy as np


class Bingo:
    def __init__(self):
        self.board = []

    def add_line(self, line):
        self.board.append(line)

    def solve(self, number):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == number:
                    self.board[i][j] = None

    def victory(self):
        arr_2d = np.array(self.board)
        for i in range(arr_2d.shape[0]):
            if np.all(arr_2d[i] == None):
                return True
        trans_arr = arr_2d.T
        for i in range(trans_arr.shape[0]):
            if np.all(trans_arr[i] == None):
                return True
        return False

    def get_score(self):
        score = 0
        for row in self.board:
            for col in row:
                if col is not None:
                    score += col
        return score

    def __str__(self):
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print()
        return ''


def read_input():
    with open('input4.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        input = [int(number) for number in lines[0].split(',')]
        bingos = []
        bingo = Bingo()
        for line in lines[2:]:
            if line == '':
                bingos.append(bingo)
                bingo = Bingo()
            else:
                bingo.add_line([int(number) for number in line.split(' ') if number != ''])
        bingos.append(bingo)
        return input, bingos


def part1():
    input, bingos = read_input()
    score = []
    for number in input:
        for bingo in bingos:
            bingo.solve(number)
            if bingo.victory():
                score.append(bingo.get_score() * number)
        if score:
            break
    return max(score)


def part2():
    input, bingos = read_input()
    victories = np.zeros(len(bingos))
    last_victory = None
    for number in input:
        for i, bingo in enumerate(bingos):
            if victories[i] == 1:
                continue
            bingo.solve(number)
            if bingo.victory():
                last_victory = bingo
                victories[i] = 1
        if np.all(victories == 1):
            return last_victory.get_score() * number


if __name__ == '__main__':
    print(part1())
    print(part2())
