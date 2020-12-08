#!/usr/bin/env python3

# https://adventofcode.com/2020/day/8

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line for line in file]


def get_accumulator_value(data):
    accumulator = 0
    index = 0
    visited = [0] * len(data)
    while index < len(data) and visited[index] == 0:
        visited[index] = 1
        instruction, num = data[index].split()
        num = int(num)
        if instruction == "acc":
            accumulator += num
            index += 1
        elif instruction == "nop":
            index += 1
        elif instruction == "jmp":
            index += num
    return index, accumulator


def solve(data, change_instruction=False):
    accumulator = 0
    index = 0
    if not change_instruction:
        return get_accumulator_value(data)[1]
    else:
        for i in range(len(data)):
            instruction, num = data[i].split()
            if instruction == "jmp":
                data[i] = "nop" + data[i][3:]
                index, accumulator = get_accumulator_value(data)
                data[i] = "jmp" + data[i][3:]

            elif instruction == "nop":
                data[i] = "jmp" + data[i][3:]
                index, accumulator = get_accumulator_value(data)
                data[i] = "nop" + data[i][3:]

            if index == len(data):
                return accumulator


def get_output_1(data):
    print(solve(data))


def get_output_2(data):
    print(solve(data, True))


get_output_1(lines)
get_output_2(lines)
