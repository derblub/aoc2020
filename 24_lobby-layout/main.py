#!/usr/bin/env python3

# https://adventofcode.com/2020/day/24

import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    lines = [line.rstrip("\n") for line in file]


# thanks to https://www.redblobgames.com/grids/hexagons/
def get_black_tiles(tiles):
    black_tiles = set()
    for line in tiles:
        x, y, z = 0, 0, 0
        i = 0
        while line:
            if line.startswith('e'):
                x += 1
                y -= 1
                line = line[1:]
            elif line.startswith('se'):
                y -= 1
                z += 1
                line = line[2:]
            elif line.startswith('sw'):
                x -= 1
                z += 1
                line = line[2:]
            elif line.startswith('w'):
                x -= 1
                y += 1
                line = line[1:]
            elif line.startswith('nw'):
                z -= 1
                y += 1
                line = line[2:]
            elif line.startswith('ne'):
                x += 1
                z -= 1
                line = line[2:]
            else:
                assert False
        if (x, y, z) in black_tiles:
            black_tiles.remove((x, y, z))
        else:
            black_tiles.add((x, y, z))
    return black_tiles


def get_output_1(tiles):
    print(len(get_black_tiles(tiles)))


def get_output_2(tiles):
    black_tiles = get_black_tiles(tiles)
    for _ in range(100):
        new_black_tiles = set()
        checked_tiles = set()
        for (x, y, z) in black_tiles:
            checked_tiles.add((x, y, z))
            for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
                checked_tiles.add((x + dx, y + dy, z + dz))

        for (x, y, z) in checked_tiles:
            nbr = 0
            for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
                if (x + dx, y + dy, z + dz) in black_tiles:
                    nbr += 1
            if (x, y, z) in black_tiles and (nbr == 1 or nbr == 2):
                new_black_tiles.add((x, y, z))
            if (x, y, z) not in black_tiles and nbr == 2:
                new_black_tiles.add((x, y, z))

        black_tiles = new_black_tiles
    print(len(black_tiles))


get_output_1(lines)
get_output_2(lines)
