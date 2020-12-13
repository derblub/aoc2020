#!/usr/bin/env python3

# https://adventofcode.com/2020/day/13

import os
import sys
from functools import reduce

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n").split(',') for line in file]

earliest_depart = int(lines[0][0])
buses_in_service = [(i, int(b)) for i, b in enumerate(lines[1]) if b != 'x']


def chinese_remainder_theorem(n, a):
    """ https://rosettacode.org/wiki/Chinese_remainder_theorem """
    end_sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        end_sum += a_i * modular__multiplicative_inverse(p, n_i) * p
    return end_sum % prod


def modular__multiplicative_inverse(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_output_1(start, buses):
    wait, bus = min((abs(start % (-b)), b) for _, b in buses)
    print(wait * bus)


def get_output_2(buses):
    n = a = []
    for i, bus in buses:
        n.append(bus)
        a.append(bus - i)
    print(chinese_remainder_theorem(n, a))


get_output_1(earliest_depart, buses_in_service)
get_output_2(buses_in_service)
