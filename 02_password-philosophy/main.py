#!/usr/bin/env python3

# https://adventofcode.com/2020/day/2

import os
import sys
import re


with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def parse_passwords():
    return [re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups() for line in lines]


def get_output_1(data):
    print(sum(int(min_count) <= password.count(character) <= int(max_count) for min_count, max_count, character, password in data))


def get_output_2(data):
    print(sum([password[int(min_count)-1], password[int(max_count)-1]].count(character) == 1 for min_count, max_count, character, password in data))


parsed_data = parse_passwords()
get_output_1(parsed_data)
get_output_2(parsed_data)
