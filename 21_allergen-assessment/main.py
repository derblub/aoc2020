#!/usr/bin/env python3

# https://adventofcode.com/2020/day/21

import os
import sys
import regex

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


def parse_foods(data):
    candidates = {}
    ingredients = []
    for line in data:
        match = regex.search(r'(?:(?P<ingredients>\w+)(?: )?)+\(contains (?:(?P<allergens>\w+)(?:, )?)+\)', line).capturesdict()
        ingredients.extend(match['ingredients'])
        for allergen in match['allergens']:
            if allergen in candidates:
                candidates[allergen] &= set(match['ingredients'])
            else:
                candidates[allergen] = set(match['ingredients'])
    return candidates, ingredients


def get_output(data):
    candidates, ingredients = parse_foods(data)
    found = {}
    while candidates:
        for allergen, ingredient in list(candidates.items()):
            if len(ingredient) == 1:
                found[allergen] = min(ingredient)
                del candidates[allergen]
            else:
                candidates[allergen] -= set(found.values())
    print(len([ingredient for ingredient in ingredients if ingredient not in found.values()]))
    print(','.join([v for k,v in sorted(found.items())]))


get_output(lines)
