#!/usr/bin/env python3

# https://adventofcode.com/2020/day/6

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    answers = [group.splitlines() for group in file.read().split('\n\n')]


def get_output(data):
    total_1 = total_2 = 0
    for group in data:
        answer = ''.join(group)
        for letter in set(answer):
            total_1 += 1
            if answer.count(letter) == len(group):
                total_2 += 1
    print(total_1)
    print(total_2)


get_output(answers)
