import re
from collections.abc import Iterator

ODD_DIRS = {
    'e':  [1, 0],
    'w':  [-1, 0],
    'nw': [0, -1],
    'ne': [1, -1],
    'sw': [0, 1],
    'se': [1, 1]
}

EVEN_DIRS = {
    'e':  [1, 0],
    'w':  [-1, 0],
    'nw': [-1, -1],
    'ne': [0, -1],
    'sw': [-1, 1],
    'se': [0, 1]
}

def set_initial_tiles(tiles: Iterator[list[str]]) -> set:
    black_tiles = set()
    for tile in tiles:
        pos = [0, 0]
        for instruction in tile:
            dirs = EVEN_DIRS if pos[1] % 2 == 0 else ODD_DIRS
            pos[0] += dirs[instruction][0]
            pos[1] += dirs[instruction][1]
        pos_t = tuple(pos)
        if pos_t in black_tiles:
            black_tiles.remove(pos_t)
        else:
            black_tiles.add(pos_t)
    return black_tiles

def adj_tiles(tile: tuple[int, int], black_tiles: set) -> tuple[set, set]:
    white_adj = set()
    black_adj = set()
    dirs = EVEN_DIRS if tile[1] % 2 == 0 else ODD_DIRS
    for direction in dirs.values():
        adj = (tile[0]+direction[0], tile[1]+direction[1])
        if adj in black_tiles:
            black_adj.add(adj)
        else:
            white_adj.add(adj)
    return black_adj, white_adj

def timestep(black_tiles: set) -> set:
    new_black_tiles = set()
    white_tiles = set()
    for tile in black_tiles:
        black_adj, white_adj = adj_tiles(tile, black_tiles)
        white_tiles.update(white_adj)
        if len(black_adj) not in (0, 3, 4, 5, 6):
            new_black_tiles.add(tile)
    for tile in white_tiles:
        black_adj, white_adj = adj_tiles(tile, black_tiles)
        if len(black_adj) == 2:
            new_black_tiles.add(tile)
    return new_black_tiles

with open('input') as f:
    tiles = f.read().splitlines()

TILES_RE = re.compile('(e|se|sw|w|nw|ne)')
tiles = (TILES_RE.findall(tile) for tile in tiles)

black_tiles = set_initial_tiles(tiles)
for _ in range(100):
    black_tiles = timestep(black_tiles)

print(len(black_tiles))