#!/usr/bin/env python3

# https://adventofcode.com/2020/day/10

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [int(line.rstrip("\n")) for line in file]
    lines.append(max(lines) + 3)


def get_output_1(adapters):
    effective = 0
    t, o = (0, 0)
    while adapters:
        if effective + 1 in adapters:
            effective += 1
            o += 1
        elif effective + 3 in adapters:
            effective += 3
            t += 1
        adapters.remove(effective)

    print(t * o)


def get_output_2(adapters):
    adapters.append(0)
    adapters.sort()

    paths = [0] * (max(adapters) + 1)
    paths[0] = 1

    for i in range(1, max(adapters) + 1):
        for j in range(1, 4):
            if i - j in adapters:
                paths[i] += paths[i - j]

    print(paths[-1])


get_output_1(lines.copy())
get_output_2(lines.copy())
