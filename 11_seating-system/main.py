#!/usr/bin/env python3

# https://adventofcode.com/2020/day/11

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def check_seat(seat):
    if seat == "L":
        return 0
    if seat == "#":
        return 1
    return 0


def check_adjacent_seats(grid, row, col):
    row_count, col_count = len(grid), len(grid[0])
    if grid[row][col] == ".":
        return "."
    occupied = 0
    for i in range(max(row - 1, 0), min(row_count, row + 2)):
        for j in range(max(col - 1, 0), min(col_count, col + 2)):
            if not (i == row and j == col):
                occupied += check_seat(grid[i][j])
    return occupied


def check_visible_seats(grid, row, col):
    if grid[row][col] == ".":
        return "."
    occupied = 0
    occupied += check_horizontal(grid, row, col)
    occupied += check_vertical(grid, row, col)
    occupied += check_diagonal(grid, row, col)
    return occupied


def check_horizontal(grid, row, col):
    col_count = len(grid[0])
    count = 0
    # right
    for j in range(col + 1, col_count):
        if grid[row][j] == "#" or grid[row][j] == "L":
            if grid[row][j] == "#":
                count += 1
            break
    # left
    for j in range(col - 1, -1, -1):
        if grid[row][j] == "#" or grid[row][j] == "L":
            if grid[row][j] == "#":
                count += 1
            break
    return count


def check_vertical(grid, row, col):
    row_count = len(grid)
    count = 0
    # down
    for i in range(row + 1, row_count):
        if grid[i][col] == "#" or grid[i][col] == "L":
            if grid[i][col] == "#":
                count += 1
            break
    # up
    for i in range(row - 1, -1, -1):
        if grid[i][col] == "#" or grid[i][col] == "L":
            if grid[i][col] == "#":
                count += 1
            break
    return count


def check_diagonal(grid, row, col):
    row_count, col_count = len(grid), len(grid[0])
    count = 0
    # down right
    i, j = row, col
    while i < row_count - 1 and j < col_count - 1:
        i += 1
        j += 1
        if grid[i][j] == "#" or grid[i][j] == "L":
            if grid[i][j] == "#":
                count += 1
            break
    # up left
    i, j = row, col
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if grid[i][j] == "#" or grid[i][j] == "L":
            if grid[i][j] == "#":
                count += 1
            break
    # up right
    i, j = row, col
    while i > 0 and j < col_count - 1:
        i -= 1
        j += 1
        if grid[i][j] == "#" or grid[i][j] == "L":
            if grid[i][j] == "#":
                count += 1
            break
    # down left
    i, j = row, col
    while i < row_count - 1 and j > 0:
        i += 1
        j -= 1
        if grid[i][j] == "#" or grid[i][j] == "L":
            if grid[i][j] == "#":
                count += 1
            break
    return count


def run_function(grid, callback, seats_to_check):
    row_count, col_count = len(grid), len(grid[0])
    grid_copy = grid.copy()
    occupied_count = 0
    for i in range(row_count):
        for j in range(col_count):
            occupied = callback(grid, i, j)
            if grid[i][j] == "L" and occupied == 0:
                grid_copy[i] = grid_copy[i][:j] + "#" + grid_copy[i][j + 1:]
            elif grid[i][j] == "#" and occupied >= seats_to_check:
                grid_copy[i] = grid_copy[i][:j] + "L" + grid_copy[i][j + 1:]
            if grid_copy[i][j] == "#":
                occupied_count += 1
    return grid_copy, occupied_count


def get_output(grid, callback, seats_to_check):
    count = 0
    occupied_seats = [0]
    for _ in range(100):
        grid, count = run_function(grid, callback, seats_to_check)
        occupied_seats.append(count)
        if occupied_seats[-1] - occupied_seats[-2] == 0:
            print(count)
            break
    return grid, count


get_output(lines, check_adjacent_seats, 4)
get_output(lines, check_visible_seats, 5)
