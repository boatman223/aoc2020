import re

odd_lookup = {
    'e': [1, 0],
    'w': [-1, 0],
    'nw': [0, -1],
    'ne': [1, -1],
    'sw': [0, 1],
    'se': [1, 1]
}

even_lookup = {
    'e': [1, 0],
    'w': [-1, 0],
    'nw': [-1, -1],
    'ne': [0, -1],
    'sw': [-1, 1],
    'se': [0, 1]
}

def set_initial_tiles(tiles):
    black_tiles = set()
    for tile in tiles:
        pos = [0, 0]
        for instruction in tile:
            lookup = even_lookup if pos[1] % 2 == 0 else odd_lookup
            pos[0] += lookup[instruction][0]
            pos[1] += lookup[instruction][1]
        pos_t = tuple(pos)
        if pos_t in black_tiles:
            black_tiles.remove(pos_t)
        else:
            black_tiles.add(pos_t)
    return black_tiles

def adj_tiles(tile, black_tiles):
    white_adj = set()
    black_adj = set()
    lookup = even_lookup if tile[1] % 2 == 0 else odd_lookup
    for direction in lookup.values():
        adj = (tile[0]+direction[0], tile[1]+direction[1])
        if adj in black_tiles:
            black_adj.add(adj)
        else:
            white_adj.add(adj)
    return black_adj, white_adj

def timestep(black_tiles):
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
tiles = [TILES_RE.findall(tile) for tile in tiles]

black_tiles = set_initial_tiles(tiles)
for _ in range(100):
    black_tiles = timestep(black_tiles)

print(len(black_tiles))