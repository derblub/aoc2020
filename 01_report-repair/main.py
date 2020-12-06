#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1

import os
import sys
import itertools

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [int(line.rstrip("\n")) for line in file]

final_sum = 2020


def get_output_1(data):
    for pair in itertools.combinations(data, 2):
        if sum(pair) == final_sum:
            print(pair[0] * pair[1])
            return


def get_output_2(data):
    for pair in itertools.combinations(data, 3):
        if sum(pair) == final_sum:
            print(pair[0] * pair[1] * pair[2])
            return


get_output_1(lines)
get_output_2(lines)
