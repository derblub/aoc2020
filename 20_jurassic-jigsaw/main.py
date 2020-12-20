#!/usr/bin/env python3

# https://adventofcode.com/2020/day/20

import os
import sys
import re
import math

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    tiles_input = [line.rstrip("\n") for line in file.read().strip().split('\n\n')]


def parse_tiles(data):
    tiles = {}
    for tile in data:
        rows = tile.splitlines()
        match = re.fullmatch('Tile (\d+):', rows[0])
        tile_id = int(match.group(1))
        grid = [list(col) for col in rows[1:]]
        tiles[tile_id] = grid
    return tiles


def get_edges(tile):
    yield ''.join(tile[0])  # top
    yield ''.join(tile[-1])  # bottom
    yield ''.join([row[0] for row in tile])  # left
    yield ''.join([row[-1] for row in tile])  # right


def get_output_1(tiles):
    grid = parse_tiles(tiles)
    borders = dict()
    border_counts = dict()
    for tile_id in grid:
        borders[tile_id] = set()
        for border in get_edges(grid[tile_id]):
            for border in [border, border[::-1]]:
                borders[tile_id].add(border)
                border_counts[border] = border_counts.get(border, 0) + 1

    edge_sums = [(tile_id, sum([border_counts[border] for border in borders[tile_id]])) for tile_id in borders.keys()]
    corners_product = math.prod([tile_id for (tile_id, edge_sum) in edge_sums if edge_sum == 12])
    print(corners_product)


get_output_1(tiles_input)
