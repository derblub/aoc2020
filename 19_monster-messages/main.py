#!/usr/bin/env python3

# https://adventofcode.com/2020/day/19

import os
import sys
import re

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    rules, messages = [line.rstrip("\n") for line in file.read().strip().split('\n\n')]

rules = dict([rule.split(': ', 1) for rule in rules.split('\n')])
messages = messages.split('\n')


def get_pattern(rule_number, replace=False):
    if replace:
        if rule_number == '8':
            return get_pattern('42', replace) + '+'
        elif rule_number == '11':
            a = get_pattern('42', replace)
            b = get_pattern('31', replace)
            return '(?:' +\
                        '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) +\
                   ')'

    rule = rules[rule_number]
    if re.fullmatch(r'"."', rule):
        return rule[1]
    else:
        parts = rule.split(' | ')
        result = []
        for part in parts:
            numbers = part.split(' ')
            result.append(''.join(get_pattern(number, replace) for number in numbers))
        return '(?:' + '|'.join(result) + ')'


def count_valid(data, replace=False):
    pattern = get_pattern('0', replace)
    count = 0
    for message in data:
        count += bool(re.fullmatch(pattern, message))
    return count

def get_output_1(data):
    print(count_valid(data))

def get_output_2(data):
    print(count_valid(data, True))


get_output_1(messages)
get_output_2(messages)
