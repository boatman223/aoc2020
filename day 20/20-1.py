with open('input') as f:
    tiles = [x.split() for x in f.read().split('\n\n')]

def parse_tiles(tiles):
    parsed_tiles = {}
    for tile in tiles:
        number = int(tile[1][:-1])
        edge1 = tile[2]
        edge2 = tile[-1]
        edge3 = ''.join([x[0] for x in tile[2:]])
        edge4 = ''.join([x[-1] for x in tile[2:]])
        parsed_tiles[number] = [edge1, edge2, edge3, edge4]

    return parsed_tiles

tiles = parse_tiles(tiles)

total = 1
for id, edges in tiles.items():
    matches = 0
    for edge in edges:
        for id2, edges2 in tiles.items():
            if id != id2 and edge in edges2 or edge[::-1] in edges2:
                matches += 1
    if matches == 2:
        total *= id

print(total)