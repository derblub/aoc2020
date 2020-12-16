#!/usr/bin/env python3

# https://adventofcode.com/2020/day/16

import os
import sys
import re
import math

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    input_data = [group for group in file.read().strip().split('\n\n')]

    ticket_rules = {rule[0]: tuple(map(int, rule[1:])) for rule in re.findall(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$', input_data[0], re.MULTILINE)}
    my_ticket = tuple(map(int, re.findall(r'your ticket:\n((?:\d+,)+\d+)', input_data[1])[0].split(',')))
    nearby_tickets = [tuple(map(int, ticket.split(','))) for ticket in re.findall(r'nearby tickets:\n((?:(?:\d+,)+\d+\n?)+)', input_data[2])[0].split('\n')]


def is_valid(value, rules):
    return (rules[0] <= value <= rules[1]) or (rules[2] <= value <= rules[3])


def get_limits(rules):
    min_1 = min([values[0] for key, values in rules.items()])
    max_1 = max([values[1] for key, values in rules.items()])
    min_2 = min([values[2] for key, values in rules.items()])
    max_2 = max([values[3] for key, values in rules.items()])
    return min_1, max_1, min_2, max_2


def get_output_1(rules, nearby):
    limits = get_limits(rules)
    invalid = sum([sum([value for value in ticket if not is_valid(value, limits)]) for ticket in nearby])
    print(invalid)


def get_output_2(rules, ticket, nearby):
    invalid = []
    limits = get_limits(rules)

    for data in nearby:
        if not all([is_valid(value, limits) for value in data]):
            invalid.append(data)

    for data in invalid:
        nearby.remove(data)

    tags = {key: [] for key in rules}
    for key, limit in rules.items():
        for i in range(len(rules)):
            if all([is_valid(value, limit) for value in [data[i] for data in nearby]]):
                tags[key].append(i)

    taken = []
    for key, limit in sorted(rules.items(), key=lambda x: len(tags[x[0]])):
        tags[key] = [tag for tag in tags[key] if tag not in taken][0]
        taken.append(tags[key])

    result = math.prod([ticket[tags[key]] for key in rules if key.startswith('departure')])
    print(result)


get_output_1(ticket_rules, nearby_tickets)
get_output_2(ticket_rules, my_ticket, nearby_tickets)
