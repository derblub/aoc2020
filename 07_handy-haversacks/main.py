#!/usr/bin/env python3

# https://adventofcode.com/2020/day/7

import os
import sys
from collections import defaultdict

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]

d = defaultdict(list)
d2 = defaultdict(list)

for line in lines:
    color1 = " ".join(line.split()[:2])
    chunks = line.split("contain ")[1].split(", ")
    for chunk in chunks:
        color2 = " ".join(chunk.split()[1:3])
        d[color2].append(color1)
        q = chunk.split()[0]
        if q == "no":
            d2[color1].append((color2, 0))
        else:
            d2[color1].append((color2, int(q)))


def check(color, k):
    for char in d[color]:
        k.add(char)
        check(char, k)
    return k


print(len(check("shiny gold", set())))


def count(color):
    return 1 + sum(n * count(char) for char, n in d2[color] if n > 0)


print(count("shiny gold") - 1)
