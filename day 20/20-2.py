import regex

class Tile:
    UNKNOWN = 0
    CORNER = 2
    EDGE = 3
    MIDDLE = 4

    tiles = []

    def __init__(self, tile):
        self.id = int(tile[1][:-1])
        self.type = Tile.UNKNOWN
        self.tile = tile[2:]
        edge0 = self.tile[0]
        edge90 = ''.join([x[-1] for x in self.tile])
        edge180 = tile[-1]
        edge270 = ''.join([x[0] for x in self.tile])
        self.edges = {0: edge0, 90: edge90, 180: edge180, 270: edge270}
        self.flipped_edges = {0: edge0[::-1], 90: edge90[::-1], 180: edge180[::-1], 270: edge270[::-1]}
        self.connections = []
        self.coordinates = []

    def row(self, num):
        return self.tile[num]

    def col(self, num):
        return ''.join([x[num] for x in self.tile])

    def rotate90(self):
        new_tile = []
        edge0 = self.edges[270][::-1]
        edge90 = self.edges[0]
        edge180 = self.edges[90][::-1]
        edge270 = self.edges[180]
        for i in range(10):
            new_tile.append(self.col(i)[::-1])
        self.tile = new_tile[:]
        self.edges = {0: edge0, 90: edge90, 180: edge180, 270: edge270}
        self.flipped_edges = {0: edge0[::-1], 90: edge90[::-1], 180: edge180[::-1], 270: edge270[::-1]}

    def flip_h(self):
        new_tile = []
        edge0 = self.edges[0][::-1]
        edge90 = self.edges[270]
        edge180 = self.edges[180][::-1]
        edge270 = self.edges[90]
        for i in range(10):
            new_tile.append(self.row(i)[::-1])
        self.tile = new_tile[:]
        self.edges = {0: edge0, 90: edge90, 180: edge180, 270: edge270}
        self.flipped_edges = {0: edge0[::-1], 90: edge90[::-1], 180: edge180[::-1], 270: edge270[::-1]}

    def flip_v(self):
        new_tile = []
        edge0 = self.edges[180]
        edge90 = self.edges[90][::-1]
        edge180 = self.edges[0]
        edge270 = self.edges[270][::-1]
        for i in reversed(range(10)):
            new_tile.append(self.row(i))
        self.tile = new_tile[:]
        self.edges = {0: edge0, 90: edge90, 180: edge180, 270: edge270}
        self.flipped_edges = {0: edge0[::-1], 90: edge90[::-1], 180: edge180[::-1], 270: edge270[::-1]}

    def stripped_borders(self):
        new_tile = []
        for row in self.tile[1:-1]:
            new_tile.append(row[1:-1])

        return new_tile

    def print_tile(self):
        print(f'\nTile #{self.id}')
        for row in self.tile:
            print(row)
        print('')

        return None

def orient_tiles(tiles):
    normal_match = {
        0: {
            0: ('flip_v',),
            90: ('rotate90', 'flip_h'),
            180: (),
            270: ('rotate90', 'rotate90', 'rotate90'),
        },
        90: {
            0: ('rotate90', 'flip_h'),
            90: ('flip_h',),
            180: ('rotate90',),
            270: (),
        },
    }

    flipped_match = {
        0: {
            0: ('rotate90', 'rotate90'),
            90: ('rotate90',),
            180: ('flip_h',),
            270: ('rotate90', 'flip_v'),
        },
        90: {
            0: ('rotate90', 'rotate90', 'rotate90'),
            90: ('rotate90', 'rotate90'),
            180: ('rotate90', 'flip_v'),
            270: ('flip_v',),
        },
    }

    coords = {
        0: [0, 1],
        90: [1, 0],
        180: [0, -1],
        270: [-1, 0],
    }

    queue = [tiles[0]]
    oriented = [tiles[0]]
    while queue:
        center = queue.pop()
        for angle, edge in center.edges.items():
            for tile in tiles:
                if tile not in oriented and center != tile:
                    for angle2, edge2 in tile.edges.items():
                        if edge == edge2:
                            a1 = angle if angle in (0, 90) else ((angle - 180) % 360)
                            a2 = angle2 if angle in (0, 90) else ((angle2 - 180) % 360)
                            for op in normal_match[a1][a2]:
                                getattr(tile, op)()
                            tile.coordinates = [coords[angle][0]+center.coordinates[0], coords[angle][1]+center.coordinates[1]]
                            oriented.append(tile)
                            queue.append(tile)
                    for angle2, edge2 in tile.flipped_edges.items():
                        if edge == edge2:
                            a1 = angle if angle in (0, 90) else ((angle - 180) % 360)
                            a2 = angle2 if angle in (0, 90) else ((angle2 - 180) % 360)
                            for op in flipped_match[a1][a2]:
                                getattr(tile, op)()
                            tile.coordinates = [coords[angle][0]+center.coordinates[0], coords[angle][1]+center.coordinates[1]]
                            oriented.append(tile)
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
    row = 0
    image = []
    for tile in sorted(Tile.tiles, key=lambda x: (x.coordinates[1], x.coordinates[0])):
        stripped_tile = tile.stripped_borders()
        for i in range(8):
            try: image[tile.coordinates[1]*8+i] += stripped_tile[i]
            except: image.append(stripped_tile[i])

    return image

def find_monsters(image):

    def flip_image(image):
        new_image = []
        for line in image:
            new_image.append(line[::-1])

        return new_image

    def rotate_image(image):
        new_image = []
        for i in range(len(image[0])):
            new_image.append(''.join([x[i] for x in image])[::-1])

        return new_image

    monsters = 0
    for _ in range(2):
        for __ in range(4):
            for row, line in enumerate(image):
                if matches := regex.finditer('.#..#..#..#..#..#...', line, overlapped=True):
                    for match in matches:
                        if regex.match('#....##....##....###', image[row-1][match.start():match.end()]):
                            if regex.match('..................#.', image[row-2][match.start():match.end()]):
                                monsters += 1
            if monsters:
                break
            image = rotate_image(image)
        else:
            image = flip_image(image)
            continue
        break

    return image, monsters

def get_solution(image, monsters):
    total = 0
    for line in image:
        total += line.count('#')
    total -= (monsters*15)

    return total

with open('input') as f:
    tiles = [x.split() for x in f.read().split('\n\n')]

for tile in tiles:
    Tile.tiles.append(Tile(tile))

Tile.tiles[0].coordinates = [0, 0]
orient_tiles(Tile.tiles)
adjust_origin(Tile.tiles)
image = build_image(Tile.tiles)
image, monsters = find_monsters(image)
solution = get_solution(image, monsters)

print(solution)