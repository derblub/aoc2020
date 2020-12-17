#!/usr/bin/env python3

# https://adventofcode.com/2020/day/17

import os
import sys
import itertools
from collections import defaultdict

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def get_active(data, dimensions):
    positions = []
    for x in range(len(data)):
        for y in range(len(data)):
            if data[x][y] == "#":
                positions.append((x, y, *([0] * (dimensions - 2))))
    return positions


def get_active_neighbours(active, dimensions):
    neighbours = defaultdict(lambda: 0)
    for position in active:
        for step in itertools.product([x for x in range(-1, 2)], repeat=dimensions):
            if step != tuple(0 for x in range(dimensions)):
                tup = tuple(i + j for i, j in zip(position, step))
                neighbours[tup] += 1
    return neighbours


def run_cycles(data, dimensions, cycles):
    active = new = get_active(data, dimensions)
    for _ in range(cycles):
        new = []
        neighbors = get_active_neighbours(active, dimensions)
        for k, v in neighbors.items():
            if (v == 2 and k in active) or v == 3:
                new.append(k)
        active = new
    return len(new)


print(run_cycles(lines, 3, 6))
print(run_cycles(lines, 4, 6))
