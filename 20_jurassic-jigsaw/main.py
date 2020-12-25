#!/usr/bin/env python3

# https://adventofcode.com/2020/day/20

import os
import sys
import re
import math

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    tiles_input = [line.rstrip("\n") for line in file.read().strip().split('\n\n')]


MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


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
    return tile[0], [l[-1] for l in tile], tile[-1], [l[0] for l in tile]


def get_flips(tile):
    return [tile, tile[::-1], [l[::-1] for l in tile], [l[::-1] for l in tile][::-1]]


def get_rotations(tile):
    rots = [tile]
    last = tile
    for _ in range(3):
        tile = [l[:] for l in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x]) - y - 1][x]
        last = tile
        rots.append(tile)
    return rots


def get_transforms(tile):
    possible = []
    for flip in get_flips(tile):
        possible.extend(get_rotations(flip))
    output = []
    for pos in possible:
        if pos not in output:
            output.append(pos)
    return output


def record_tile(tiled, tile_meta, dimension, x=0, y=0, seen=None):
    if seen is None:
        seen = set()
    if y == dimension:
        return tiled
    next_x = x + 1
    next_y = y
    if next_x == dimension:
        next_x = 0
        next_y += 1
    for id, tiles in tile_meta.items():
        if id in seen:
            continue
        seen.add(id)
        for transId, border in tiles.items():
            top, _, _, left = border

            if x > 0:
                neighbor, neighbor_transform = tiled[x - 1][y]
                _, neighbor_right, _, _ = tile_meta[neighbor][neighbor_transform]
                if neighbor_right != left:
                    continue
            if y > 0:
                neighbor, neighbor_transform = tiled[x][y - 1]
                _, _, neighbor_bottom, _ = tile_meta[neighbor][neighbor_transform]
                if neighbor_bottom != top:
                    continue
            tiled[x][y] = (id, transId)
            ans = record_tile(tiled, tile_meta, dimension, x=next_x, y=next_y, seen=seen)
            if ans is not None:
                return ans
        seen.remove(id)
    tiled[x][y] = None
    return None


def get_tiled(tiles):
    tile_meta = {id: get_transforms(tile) for id, tile in tiles.items()}
    tile_border_meta = {}
    for id, tiles in tile_meta.items():
        for idx, tile in enumerate(tiles):
            if id not in tile_border_meta.keys():
                tile_border_meta[id] = {}
            tile_border_meta[id][idx] = get_edges(tile)
    dimension = math.isqrt(len(tile_meta))
    tiled = [[None] * dimension for _ in range(dimension)]
    return tile_meta, record_tile(tiled, tile_border_meta, dimension)


def get_output_1(tiled):
    print(tiled[0][0][0] * tiled[0][-1][0] * tiled[-1][0][0] * tiled[-1][-1][0])


def strip_border(tile_meta, tiled):
    out = []
    for row in tiled:
        tiles = []
        for number, transform_id in row:
            tile = tile_meta[number][transform_id]
            tiles.append([l[1:-1] for l in tile[1:-1]])
        for y in range(len(tiles[0][0])):
            new_row = []
            for id in range(len(tiles)):
                new_row.extend(tiles[id][x][y] for x in range(len(tiles[id])))
            out.append(new_row)
    return out


def search_monster():
    monster_locations = []
    max_x, max_y = 0, 0
    for y2, line in enumerate(MONSTER.splitlines()):
        for x2, char in enumerate(line):
            if char == "#":
                monster_locations.append((x2, y2))
                max_x = max(x2, max_x)
                max_y = max(y2, max_y)
    return monster_locations, max_x, max_y


def check_monsters(grid):
    monster_locations, max_x, max_y = search_monster()
    monster_spots = set()
    for y in range(len(grid)):
        if y + max_y >= len(grid):
            break
        for x in range(len(grid[y])):
            if x + max_x >= len(grid[y]):
                break
            is_monster = True
            for xOff, yOff in monster_locations:
                if grid[y + yOff][x + xOff] != "#":
                    is_monster = False
                    break
            if is_monster:
                for dx, dy in monster_locations:
                    monster_spots.add((x + dx, y + dy))
    if len(monster_spots) == 0:
        return None
    fields = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '#':
                fields.add((x, y))
    return len(fields - monster_spots)


def get_output_2(tile_meta, tiled):
    grid = strip_border(tile_meta, tiled)
    grid_options = get_transforms(grid)

    for opt in grid_options:
        ans = check_monsters(opt)
        if ans is not None:
            print(ans)


tiles = parse_tiles(tiles_input)
tile_meta, tiled = get_tiled(tiles)


get_output_1(tiled)
get_output_2(tile_meta, tiled)
