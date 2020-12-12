#!/usr/bin/env python3

# https://adventofcode.com/2020/day/12

import os
import sys
import re

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    instructions = [(instruction[0], int(instruction[1])) for instruction in [re.match(r'^([A-Z])(\d+)$', line).groups() for line in file]]


directions = {'E': 0, 'S': 90, 'W': 180, 'N': 270}


def move_forward(x, y, direction, value):
    if direction == 270:
        return x, y - value
    if direction == 90:
        return x, y + value
    if direction == 0:
        return x + value, y
    if direction == 180:
        return x - value, y


def rotate(degrees, value):
    return (degrees + 360 + value) % 360


def rotate_waypoint(x, y, degrees):
    if degrees == 0:
        return x, y
    if degrees == 90:
        return -y, x
    if degrees == 180:
        return -x, -y
    if degrees == 270:
        return y, -x


def get_output_1(data):
    x, y, direction = 0, 0, directions['E']
    for key, value in data:
        if key in directions:
            x, y = move_forward(x, y, directions[key], value)
        elif key == 'F':
            x, y = move_forward(x, y, direction, value)
        elif key in ['L', 'R']:
            direction = rotate(direction, - value if key == 'L' else value)
    print(abs(x) + abs(y))


def get_output_2(data):
    x, y = 0, 0
    waypoint_x, waypoint_y = 10, -1
    for key, value in data:
        if key in directions:
            waypoint_x, waypoint_y = move_forward(waypoint_x, waypoint_y, directions[key], value)
        elif key == 'F':
            x += waypoint_x * value
            y += waypoint_y * value
        elif key in ['L', 'R']:
            waypoint_x, waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, (360 - value) if key == 'L' else value)
    print(abs(x) + abs(y))


get_output_1(instructions)
get_output_2(instructions)
