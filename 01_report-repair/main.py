#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1

import os
import sys


with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [int(line.rstrip("\n")) for line in file]

final_sum = 2020

def get_output_1(data):
    for a in range(len(data)):
        for b in range(len(data)):
            if data[a] + data[b] == final_sum:
                output = data[a] * data[b]
                print(output)
                return

def get_output_2(data):
    for a in range(len(data)):
        for b in range(len(data)):
            for c in range(len(data)):
                if data[a] + data[b] + data[c] == final_sum:
                    output = data[a] * data[b] * data[c]
                    print(output)
                    return


get_output_1(lines)
get_output_2(lines)
