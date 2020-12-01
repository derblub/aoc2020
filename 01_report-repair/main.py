#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1

import os
import sys


with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [int(line.rstrip("\n")) for line in file]

final_sum = 2020
for a in range(len(lines)):
    for b in range(len(lines)):
        if lines[a] + lines[b] == final_sum:
            output = lines[a] * lines[b]
            print(output)
            exit(1)
