#!/usr/bin/env python3

# https://adventofcode.com/2020/day/9

import os
import sys
from itertools import combinations

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [int(line.rstrip('\n')) for line in file]


def solve_preamble(data):
    number = 0
    preamble_length = 25
    for (index, number) in enumerate(data):
        if index < preamble_length:
            continue
        if number not in [x + y for x, y in combinations(data[index - preamble_length:index], 2)]:
            break
    print(number)

    index_a, index_b = 0, 0
    total = data[0]
    while total != number:
        if total < number:
            index_b += 1
            total += data[index_b]
        elif total > number:
            total -= data[index_a]
            index_a += 1
    smallest_number = min(data[index_a:index_b + 1])
    largest_number = max(data[index_a:index_b + 1])
    print(smallest_number + largest_number)


solve_preamble(lines)
