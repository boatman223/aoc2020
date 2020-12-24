import re

with open('input') as f:
    tiles = f.read().splitlines()

TILES_RE = re.compile('(e|se|sw|w|nw|ne)')
tiles = [TILES_RE.findall(tile) for tile in tiles]

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

black_tiles = set()
for tile in tiles:
    pos = [0, 0]
    for instruction in tile:
        if pos[1] % 2 == 0:
            pos[0] += even_lookup[instruction][0]
            pos[1] += even_lookup[instruction][1]
        else:
            pos[0] += odd_lookup[instruction][0]
            pos[1] += odd_lookup[instruction][1]
    pos_t = tuple(pos)
    if pos_t in black_tiles:
        black_tiles.remove(pos_t)
    else:
        black_tiles.add(pos_t)

print(len(black_tiles))