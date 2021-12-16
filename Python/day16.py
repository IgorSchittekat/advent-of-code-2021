import numpy as np
from aocd import get_data
from utils import *
import binascii

data = get_data(year=2021, day=16)


class Packet:
    def __init__(self, content):
        self.content = content

    def process(self):
        self.version = int(self.content[:3], 2)
        self.type_id = int(self.content[3:6], 2)
        if self.type_id == 4:
            self.literal, extra_packet_data = self.process_literal(self.content[6:])
            return extra_packet_data
        else:
            if self.content[6] == '0':
                length = int(self.content[7:22], 2)
                self.sub_packets = []
                sub_content = self.content[22:22 + length]
                while sub_content != '':
                    packet = Packet(sub_content)
                    sub_content = packet.process()
                    self.sub_packets.append(packet)
                try:
                    return self.content[22 + length:]
                except IndexError:
                    return ''
            else:
                self.sub_packets = []
                num_packs = int(self.content[7:18], 2)
                sub_content = self.content[18:]
                while num_packs > 0:
                    packet = Packet(sub_content)
                    sub_content = packet.process()
                    self.sub_packets.append(packet)
                    num_packs -= 1
                return sub_content

    def process_literal(self, content):
        start = 0
        number = ''
        while content[start] == '1':
            number += content[start + 1: start + 5]
            start += 5
        number += content[start + 1: start + 5]
        try:
            return int(number, 2), content[start + 5:]
        except IndexError:
            return int(number, 2), ''

    def get_all_versions(self):
        versions = [self.version]
        if self.type_id != 4:
            for packet in self.sub_packets:
                versions.extend(packet.get_all_versions())
        return versions

    def get_value(self):
        if self.type_id == 4:
            return self.literal
        else:
            sub_packets = [packet.get_value() for packet in self.sub_packets]
            if self.type_id == 0:
                return sum(sub_packets)
            elif self.type_id == 1:
                return np.prod(sub_packets)
            elif self.type_id == 2:
                return min(sub_packets)
            elif self.type_id == 3:
                return max(sub_packets)
            elif self.type_id == 5:
                return 1 if sub_packets[0] > sub_packets[1] else 0
            elif self.type_id == 6:
                return 1 if sub_packets[0] < sub_packets[1] else 0
            elif self.type_id == 7:
                return 1 if sub_packets[0] == sub_packets[1] else 0


def part1():
    h_size = len(data) * 4
    binary = bin(int(data, 16))[2:].zfill(h_size)
    packet = Packet(binary)
    packet.process()
    return sum(packet.get_all_versions())


def part2():
    h_size = len(data) * 4
    binary = bin(int(data, 16))[2:].zfill(h_size)
    packet = Packet(binary)
    packet.process()
    return packet.get_value()


if __name__ == '__main__':
    _ = "8A004A801A8002F478"
    _ = "620080001611562C8802118E34"
    _ = "C0015000016115A2E0802F182340"
    _ = "A0016C880162017C3686B18A3D4780"
    _ = "C200B40A82"
    _ = "04005AC33890"
    _ = "880086C3E88112"
    _ = "CE00C43D881120"
    _ = "D8005AC2A8F0"
    _ = "F600BC2D8F"
    _ = "9C005AC2F8F0"
    _ = "9C0141080250320F1802104A08"
    print(part1())
    print(part2())
