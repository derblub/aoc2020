#!/usr/bin/env python3

# https://adventofcode.com/2020/day/5

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def input_to_binary(data):
    data = data.replace('B', '1')
    data = data.replace('R', '1')
    data = data.replace('F', '0')
    data = data.replace('L', '0')
    return int(data, 2)


def get_seats(data):
    seats = set()
    for seat in data:
        row, col = (input_to_binary(seat[:7]), input_to_binary(seat[7:]))
        seats.add(row * 8 + col)
    return seats


def get_output_1(seats):
    print(max(get_seats(seats)))


def get_output_2(seats):
    seats = get_seats(seats)
    for i in range(127 * 8 + 7):
        if i not in seats:
            if i + 1 in seats and i - 1 in seats:
                print(i)


get_output_1(lines)
get_output_2(lines)
