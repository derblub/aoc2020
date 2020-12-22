#!/usr/bin/env python3

# https://adventofcode.com/2020/day/22

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    decks = [line.rstrip("\n") for line in file.read().strip().split('\n\n')]
    p1, p2 = [[int(card) for card in deck.split("\n")[1:]] for deck in decks]
    p1_copy = p1.copy()
    p2_copy = p2.copy()


def combat(p1_deck, p2_deck):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        first, second = p1.pop(0), p2.pop(0)
        if first > second:
            p1.extend([first, second])
        else:
            p2.extend([second, first])
    return p1_deck if len(p1_deck) > 0 else p2_deck


def recursive_combat(p1_deck, p2_deck, remaining):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        if (tuple(p1_deck), tuple(p2_deck)) in remaining:
            return 1, p1_deck

        remaining.add((tuple(p1_deck), tuple(p2_deck)))

        first, second = p1_deck.pop(0), p2_deck.pop(0)
        if len(p1_deck) >= first and len(p2_deck) >= second:
            winner, _ = recursive_combat(p1_deck[:first], p2_deck[:second], set())
        else:
            winner = 1 if first > second else 0

        if winner == 1:
            p1_deck.extend([first, second])
        else:
            p2_deck.extend([second, first])
    return (1, p1_deck) if len(p1_deck) > 0 else (0, p2_deck)


def get_output_1():
    count = 0
    for index, value in enumerate(combat(p1, p2)[::-1]):
        count += (index + 1) * value
    print(count)


def get_output_2():
    count = 0
    for index, value in enumerate(recursive_combat(p1_copy, p2_copy, set())[1][::-1]):
        count += (index + 1) * value
    print(count)


get_output_1()
get_output_2()
