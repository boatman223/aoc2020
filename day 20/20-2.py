import regex
import random

class Tile:

    tiles = []

    def __str__(self):
        out = f'Tile {self.id}\n'
        for row in self.tile:
            out += f'{row}\n'
        return out

    def __init__(self, tile):
        self.id = int(tile[1][:-1])
        self.tile = tile[2:]
        self.coordinates = []
        self.edges = {
            0:   self.tile[0],
            90:  ''.join([x[-1] for x in self.tile]),
            180: tile[-1],
            270: ''.join([x[0] for x in self.tile])
        }

    def row(self, num):
        return self.tile[num]

    def col(self, num):
        return ''.join([x[num] for x in self.tile])

    def rotate90(self):
        new_tile = [self.col(i)[::-1] for i in range(10)]
        new_edges = {
            0:   self.edges[270][::-1],
            90:  self.edges[0],
            180: self.edges[90][::-1],
            270: self.edges[180]
        }
        return new_tile, new_edges

    def flip_h(self):
        new_tile = [self.row(i)[::-1] for i in range(10)]
        new_edges = {
            0:   self.edges[0][::-1],
            90:  self.edges[270],
            180: self.edges[180][::-1],
            270: self.edges[90]
        }
        return new_tile, new_edges

    def flip_v(self):
        new_tile = [self.row(i) for i in reversed(range(10))]
        new_edges = {
            0:   self.edges[180],
            90:  self.edges[90][::-1],
            180: self.edges[0],
            270: self.edges[270][::-1]
        }
        return new_tile, new_edges

    def strip_borders(self):
        new_tile = [row[1:-1] for row in self.tile[1:-1]]
        return new_tile

def orient_tiles(tiles, starting_tile):
    normal_match = {
        0:  {
            0:   ('flip_v',),
            90:  ('rotate90', 'flip_h'),
            180: (),
            270: ('rotate90', 'rotate90', 'rotate90'),
        },
        90: {
            0:   ('rotate90', 'flip_h'),
            90:  ('flip_h',),
            180: ('rotate90',),
            270: (),
        },
    }
    flipped_match = {
        0:  {
            0:   ('rotate90', 'rotate90'),
            90:  ('rotate90',),
            180: ('flip_h',),
            270: ('rotate90', 'flip_v'),
        },
        90: {
            0:   ('rotate90', 'rotate90', 'rotate90'),
            90:  ('rotate90', 'rotate90'),
            180: ('rotate90', 'flip_v'),
            270: ('flip_v',),
        },
    }
    coords = {
        0:   [0, 1],
        90:  [1, 0],
        180: [0, -1],
        270: [-1, 0],
    }

    queue = [starting_tile]
    while queue:
        center = queue.pop()
        for angle, edge in center.edges.items():
            for tile in tiles:
                for angle2, edge2 in tile.edges.items():
                    if center != tile and edge in (edge2, edge2[::-1]):
                        a1 = angle if angle in (0, 90) else ((angle - 180) % 360)
                        a2 = angle2 if angle in (0, 90) else ((angle2 - 180) % 360)
                        match = normal_match if edge == edge2 else flipped_match
                        for op in match[a1][a2]:
                            tile.tile, tile.edges = getattr(tile, op)()
                        tile.coordinates = [coords[angle][0]+center.coordinates[0], coords[angle][1]+center.coordinates[1]]
                        tiles.remove(tile)
                        queue.append(tile)

def adjust_origin(tiles):
    min_x = 0
    max_y = 0
    for tile in tiles:
        min_x = min(min_x, tile.coordinates[0])
        max_y = max(max_y, tile.coordinates[1])
    for tile in tiles:
        tile.coordinates[0] -= min_x
        tile.coordinates[1] -= max_y
        tile.coordinates[1] = abs(tile.coordinates[1])

def build_image(tiles):
    image = []
    for tile in sorted(tiles, key=lambda x: (x.coordinates[1], x.coordinates[0])):
        stripped_tile = tile.strip_borders()
        for i in range(8):
            try: image[tile.coordinates[1]*8+i] += stripped_tile[i]
            except: image.append(stripped_tile[i])
    return image

def find_monsters(image):

    def flip_image(image):
        new_image = [line[::-1] for line in image]
        return new_image

    def rotate_image(image):
        new_image = []
        for i in range(len(image[0])):
            new_image.append(''.join([x[i] for x in image])[::-1])
        return new_image

    MONSTER1 = regex.compile('..................#.')
    MONSTER2 = regex.compile('#....##....##....###')
    MONSTER3 = regex.compile('.#..#..#..#..#..#...')
    monsters = 0
    rotates = 0
    while not monsters:
        for row, line in enumerate(image):
            if matches := regex.finditer(MONSTER3, line, overlapped=True):
                for match in matches:
                    if regex.match(MONSTER2, image[row-1][match.start():match.end()]):
                        if regex.match(MONSTER1, image[row-2][match.start():match.end()]):
                            monsters += 1
        image = rotate_image(image)
        rotates += 1
        if rotates == 4: image = flip_image(image)
        if rotates == 8: break
    return image, monsters

def get_solution(image, monsters):
    total = 0
    for line in image:
        total += line.count('#')
    total -= monsters*15
    return total

with open('input') as f:
    tiles = [x.split() for x in f.read().split('\n\n')]

Tile.tiles = [Tile(tile) for tile in tiles]
starting_tile = Tile.tiles[random.randint(0, len(Tile.tiles)-1)]
starting_tile.coordinates = [0, 0]

orient_tiles(Tile.tiles[:], starting_tile)
adjust_origin(Tile.tiles)
image = build_image(Tile.tiles)
image, monsters = find_monsters(image)
solution = get_solution(image, monsters)

print(solution)