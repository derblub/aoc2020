#!/usr/bin/env python3

# https://adventofcode.com/2020/day/5

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    input_data = [int(number) for number in file.read().strip().split(",")]


def solve(numbers, limit):
    memory = {x: n + 1 for n, x in enumerate(numbers)}
    last_number = numbers[-1]
    for turn in range(len(numbers) + 1, limit + 1):
        number = turn - 1 - memory[last_number] if last_number in memory else 0
        memory[last_number] = turn - 1
        last_number = number
    print(last_number)


def get_output_1(data):
    return solve(data, 2020)


def get_output_2(data):
    return solve(data, 30000000)


get_output_1(input_data)
get_output_2(input_data)
