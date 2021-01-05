import numpy as np
from collections import namedtuple
from math import sqrt

file = open("day20_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

tiles = {}
tile_len = 0

working_tile = None
tile = None
row = 0
for line in lines:
    if line.startswith('Tile'):
        working_tile = line.replace('Tile ', '')[:-1]
    elif line == '':
        tiles[working_tile] = tile
        tile = None
        working_tile = None
        row = 0
    else:
        if tile is None:
            tile_len = len(line)
            tile = np.zeros((tile_len, tile_len), int)
        for col in range(tile_len):
            if line[col] == '#':
                tile[row][col] = 1
        row += 1
        
Tile = namedtuple('Tile', ('id', 'frame', 'orientation'))
# orientation 0=top, 1=right, 2=bottom, 3=left


def create_tile(i, orientation=0, flippedH=False, flippedV=False):
    rotated = np.rot90(tiles[i], orientation, axes=(1, 0))
    if flippedH:
            rotated = np.fliplr(rotated)
    if flippedV:
            rotated = np.flipud(rotated)
    return Tile(i, rotated, orientation)


def get_edge(tile, edge):
    # edge = (edge + tile.orientation) % 4
    if edge == 0:
        return tile.frame[0, :]
    if edge == 1:
        return tile.frame[:, -1]
    if edge == 2:
        return tile.frame[-1, :]
    if edge == 3:
        return tile.frame[:, 0]


def test_edges(tile1, tile2, left):
    if left:
        edge1 = get_edge(tile1, 1)
        edge2 = get_edge(tile2, 3)
        return (edge1 == edge2).all()
    else:
        edge1 = get_edge(tile1, 2)
        edge2 = get_edge(tile2, 0)
        return (edge1 == edge2).all()


def get_next_states(row, col):
    ret = []
    for i in tiles.keys():
        if i in seen:
            continue
        for h in [False, True]:
            for v in [False, True]:
                if h and v:
                    continue
                for o in range(0, 4):
                    tile = create_tile(i, o, h, v)
                    fits = True
                    if row != 0:
                        fits &= test_edges(grid[row-1, col], tile, False)
                    if fits and col != 0:
                        fits &= test_edges(grid[row, col-1], tile, True)
                    if fits:
                        ret.append((tile, row, col))
    return ret


grid_len = int(sqrt(len(tiles.keys())))
grid = np.empty((grid_len, grid_len), Tile)
row = 0
col = 0
seen = set()
all_tiles = get_next_states(0, 0)
stack = []

# find all corners to prime the stack
for tile1, _, _ in all_tiles:
    left_matches = 0
    right_matches = 0
    top_matches = 0
    bottom_matches = 0

    for tile2, _, _ in all_tiles:
        if tile1.id == tile2.id:
            continue
        if test_edges(tile1, tile2, left=True):
            right_matches += 1
        if test_edges(tile2, tile1, left=True):
            left_matches += 1
        if test_edges(tile1, tile2, left=False):
            bottom_matches += 1
        if test_edges(tile2, tile1, left=False):
            top_matches += 1

    if left_matches == 0 and right_matches == 1 and top_matches == 0 and bottom_matches == 1:
        print('corner', tile1.id)
        stack.append((tile1, 0, 0))


def clear_stale_tiles(row, col):
    for i in range(grid_len):
        for j in range(grid_len):
            if i > row or i == row and j >= col:
                if grid[i, j] is not None:
                    old_id = grid[i, j].id
                    if old_id in seen:
                        seen.remove(old_id)
                    grid[i, j] = None


# DFS with backtracking
while len(stack) > 0:
    tile, row, col = stack.pop()
    clear_stale_tiles(row, col)
    grid[row, col] = tile
    seen.add(tile.id)
    
    new_col = col+1
    new_row = row
    if new_col >= grid_len:
        new_col = 0
        new_row += 1
    if new_row >= grid_len:
        # last spot filled, rejoice!
        print('done')
        break
    
    next_states = get_next_states(new_row, new_col)
    if len(next_states) == 0:
        # deadend
        grid[row, col] = None
        seen.remove(tile.id)
        continue
        
    stack += next_states

total = 1
for i in [0, -1]:
    for j in [0, -1]:
        total *= int(grid[i, j].id)

print(total)
