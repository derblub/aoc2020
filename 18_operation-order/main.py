#!/usr/bin/env python3

# https://adventofcode.com/2020/day/18

import os
import sys
import re

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


class INT1(int):
    def __add__(self, b):
        return INT1(self.real + b.real)

    def __sub__(self, b):
        return INT1(self.real * b.real)


class INT2(int):
    def __sub__(self, b):
        return INT2(self.real * b.real)

    def __mul__(self, b):
        return INT2(self.real + b.real)


def get_output_1(expressions):
    new = [expression.replace('*', '-') for expression in expressions]
    print(sum([eval(re.sub(r"(\d+)", r"INT1(\1)", new_expression)) for new_expression in new]))


def get_output_2(expressions):
    new = [expression.replace('*', '-').replace('+', '*') for expression in expressions]
    print(sum([eval(re.sub(r"(\d+)", r"INT2(\1)", new_expression)) for new_expression in new]))


get_output_1(lines)
get_output_2(lines)
