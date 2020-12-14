#!/usr/bin/env python3

# https://adventofcode.com/2020/day/14

import re
import os
import sys
from itertools import product

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    pattern = re.compile("^(\w*)\[?(\d+)?\]?\s=\s(.*)$")
    data = [pattern.findall(x) for x in file.read().splitlines()]


def apply_mask(s, m):
    m1 = int(m.replace("X", "0"), 2)
    m2 = int(m.replace("X", "1"), 2)
    return m2 & (m1 | s)


def generate_addrs(adr, mask):
    bits = format(int(adr), "036b")
    mask = mask.zfill(36)
    change = [b if m == "0" else m for b, m in zip(bits, mask)]
    to_replace = [i for i, v in enumerate(change) if v == "X"]
    floating = len(to_replace)

    for vals in product(*("01" for _ in range(floating))):
        for i, v in zip(to_replace, vals):
            change[i] = v
        yield int("".join(change), 2) % 2 ** 36 - 1


def get_output_1(instructions):
    storage = {}
    mask = ""
    for [(op, addr, val)] in instructions:
        if op == "mask":
            mask = val
        else:
            storage[int(addr)] = apply_mask(int(val), mask)
    print(sum(storage.values()))


def get_output_2(instructions):
    storage = {}
    mask = ""
    for [(op, addr, val)] in instructions:
        if op == "mask":
            mask = val
        else:
            for a in generate_addrs(addr, mask):
                storage[a] = int(val)
    print(sum(storage.values()))


get_output_1(data)
get_output_2(data)
