

class Display:
    def __init__(self, line):
        self.lenfive = []
        self.lensix = []
        self.dict = dict()
        for number in line[:10]:
            if len(number) == 2:
                self.dict[1] = set(number)
            elif len(number) == 3:
                self.dict[7] = set(number)
            elif len(number) == 4:
                self.dict[4] = set(number)
            elif len(number) == 7:
                self.dict[8] = set(number)
            elif len(number) == 5:
                self.lenfive.append(set(number))
            elif len(number) == 6:
                self.lensix.append(set(number))
        self.output = [set(number) for number in line[-4:]]

    def solve(self):
        """
          ttt
        tl   tr
        tl   tr
          mmm
        bl   br
        bl   br
          bbb
        """
        t = self.dict[7] - self.dict[1]
        tlm = self.dict[4] - self.dict[1]
        ttlm = set(list(tlm) + list(t))
        for num in self.lenfive:
            if ttlm.issubset(num):
                self.dict[5] = num
        tr = self.dict[1] - self.dict[5]
        br = self.dict[1] - tr
        for num in self.lenfive:
            if tr.issubset(num) and not br.issubset(num):
                self.dict[2] = num
            if tr.issubset(num) and br.issubset(num):
                self.dict[3] = num
        tl = self.dict[4] - self.dict[3]
        m = tlm - tl
        for num in self.lensix:
            if not m.issubset(num):
                self.dict[0] = num
            elif not tr.issubset(num):
                self.dict[6] = num
            else:
                self.dict[9] = num

    def decode(self):
        total = 0
        for number in self.output:
            if number == self.dict[0]:
                total = total * 10
            if number == self.dict[1]:
                total = total * 10 + 1
            if number == self.dict[2]:
                total = total * 10 + 2
            if number == self.dict[3]:
                total = total * 10 + 3
            if number == self.dict[4]:
                total = total * 10 + 4
            if number == self.dict[5]:
                total = total * 10 + 5
            if number == self.dict[6]:
                total = total * 10 + 6
            if number == self.dict[7]:
                total = total * 10 + 7
            if number == self.dict[8]:
                total = total * 10 + 8
            if number == self.dict[9]:
                total = total * 10 + 9
        return total


def read_input():
    with open('input8.txt', 'r') as file:
        lines = file.readlines()
        return [line.rstrip().split(' ') for line in lines]


def part1():
    outputs = [line[-4:] for line in read_input()]
    counter = 0
    for output in outputs:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                counter += 1
    return counter


def part2():
    lines = read_input()
    total = 0
    for line in lines:
        disp = Display(line)
        disp.solve()
        total += disp.decode()
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())
