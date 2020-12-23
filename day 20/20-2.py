import regex
import random
from collections.abc import Iterator

class Tile:

    tiles = []

    def __str__(self):
        out = f'Tile {self.id}\n'
        for row in self.tile:
            out += f'{row}\n'
        return out

    def __init__(self, tile: list[str]):
        self.id = int(tile[1][:-1])
        self.tile = tile[2:]
        self.coords = []
        self._edges = {}

    def row(self, num: int) -> str:
        return self.tile[num]

    def col(self, num: int) -> str:
        return ''.join([x[num] for x in self.tile])

    @property
    def edges(self) -> dict[int, str]:
        if self._edges.get(0) != self.tile[0]:
            self._edges = {
                0:   self.tile[0],
                90:  ''.join([x[-1] for x in self.tile]),
                180: self.tile[-1],
                270: ''.join([x[0] for x in self.tile])
            }
        return self._edges

    def rotate90(self) -> list[str]:
        new_tile = [self.col(i)[::-1] for i in range(10)]
        return new_tile

    def flip_h(self) -> list[str]:
        new_tile = [self.row(i)[::-1] for i in range(10)]
        return new_tile

    def flip_v(self) -> list[str]:
        new_tile = [self.row(i) for i in reversed(range(10))]
        return new_tile

    def strip_borders(self) -> list[str]:
        new_tile = [row[1:-1] for row in self.tile[1:-1]]
        return new_tile

def orient_tiles(tiles: list[Tile], starting_tile: Tile):
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
                            tile.tile = getattr(tile, op)()
                        tile.coords = [coords[angle][0]+center.coords[0], coords[angle][1]+center.coords[1]]
                        tiles.remove(tile)
                        queue.append(tile)

def build_image(tiles: list[Tile]) -> list[str]:
    y_adj = 0
    for tile in tiles:
        y_adj = max(y_adj, tile.coords[1])
    image = []
    for tile in sorted(tiles, key=lambda x: (abs(x.coords[1]-y_adj), x.coords[0])):
        tile.coords[1] = abs(tile.coords[1]-y_adj)
        stripped_tile = tile.strip_borders()
        width = len(stripped_tile[0])
        for i in range(width):
            try: image[tile.coords[1]*width+i] += stripped_tile[i]
            except IndexError: image.append(stripped_tile[i])
    return image

def find_monsters(image: list[str]) -> tuple[list[str], int]:

    def _flip_image(image: list[str]) -> list[str]:
        new_image = [line[::-1] for line in image]
        return new_image

    def _rotate_image(image: list[str]) -> list[str]:
        new_image = []
        for i in range(len(image[0])):
            new_image.append(''.join([x[i] for x in image])[::-1])
        return new_image

    def _all_orientations(image: list[str]) -> Iterator[list[str]]:
        for _ in range(2):
            for _ in range(4):
                yield image
                image = _rotate_image(image)
            image = _flip_image(image)

    MONSTER1 = regex.compile('..................#.')
    MONSTER2 = regex.compile('#....##....##....###')
    MONSTER3 = regex.compile('.#..#..#..#..#..#...')
    monsters = 0
    for orientation in _all_orientations(image):
        for row, line in enumerate(orientation):
            if matches := regex.finditer(MONSTER3, line, overlapped=True):
                for match in matches:
                    if regex.match(MONSTER2, orientation[row-1][match.start():match.end()]):
                        if regex.match(MONSTER1, orientation[row-2][match.start():match.end()]):
                            monsters += 1
        if monsters: break
    return image, monsters

def get_solution(image: list[str], monsters: int) -> int:
    total = sum((line.count('#') for line in image))
    total -= monsters*15
    return total

with open('input') as f:
    tiles = [x.split() for x in f.read().split('\n\n')]

Tile.tiles = [Tile(tile) for tile in tiles]
starting_tile = Tile.tiles[random.randint(0, len(Tile.tiles)-1)]
starting_tile.coords = [0, 0]

orient_tiles(Tile.tiles[:], starting_tile)
image = build_image(Tile.tiles)
image, monsters = find_monsters(image)
solution = get_solution(image, monsters)

print(solution)