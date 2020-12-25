#!/usr/bin/env python3

# https://adventofcode.com/2020/day/25

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    card, door = map(int, file.readlines())


def get_loop(subject, key, mod):
    power = 1
    for i in range(mod):
        power *= subject
        power %= mod
        if power == key:
            return i + 1


def get_output_1(card_key, door_key):
    subject, mod = 7, 20201227
    card_loop = get_loop(subject, card_key, mod)
    door_loop = get_loop(subject, door_key, mod)
    print(pow(subject, card_loop * door_loop, mod=mod))


get_output_1(card, door)
