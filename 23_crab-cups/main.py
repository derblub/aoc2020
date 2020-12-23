#!/usr/bin/env python3

# https://adventofcode.com/2020/day/23

cups = '476138259'


def move(circle, cup, wrap):
    pickups = []
    pick = circle[cup]
    for _ in range(3):
        pickups.append(pick)
        pick = circle[pick]

    circle[cup] = pick
    destination = cup
    while destination == cup or destination in pickups:
        destination -= 1
        if destination == 0:
            destination = wrap

    circle[pickups[-1]] = circle[destination]
    circle[destination] = pickups[0]
    return circle[cup]


def get_output_1():
    circle = [0] * 10
    numbers = [int(n) for n in cups]
    numbers.append(numbers[0])
    for i in range(9):
        circle[numbers[i]] = numbers[i+1]
    current_cup = numbers[0]

    for _ in range(100):
        current_cup = move(circle, current_cup, 9)

    result = ''
    current = circle[1]
    for _ in range(8):
        result += str(current)
        current = circle[current]
    print(result)


def get_output_2():
    circle = [0] * 1_000_001
    for i in range(10, 1_000_000):
        circle[i] = i + 1

    numbers = [int(n) for n in cups]
    for i in range(8):
        circle[numbers[i]] = numbers[i+1]
    circle[numbers[-1]] = 10
    circle[-1] = numbers[0]
    current_cup = numbers[0]
    for _ in range(10_000_000):
        current_cup = move(circle, current_cup, 1_000_000)

    print(circle[1] * circle[circle[1]])


get_output_1()
get_output_2()
