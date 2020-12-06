#!/usr/bin/env python3

# https://adventofcode.com/2020/day/3

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def count_trees_in_slopes(grid, slopes):
    tree_multiply = 1

    for slope in slopes:
        x = 0
        tree_count = 0
        for y in range(0, len(grid), slope[1]):
            if grid[y][x] == "#":
                tree_count += 1
            x = (x + slope[0]) % len(grid[0])  # infinite cols
        tree_multiply *= tree_count
    return tree_multiply


def get_output_1(grid):
    slopes = [(3, 1)]
    print(count_trees_in_slopes(grid, slopes))


def get_output_2(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(count_trees_in_slopes(grid, slopes))


get_output_1(lines)
get_output_2(lines)
