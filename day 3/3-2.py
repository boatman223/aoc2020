from collections import namedtuple
import math

with open('input') as f:
    world_map = [i.strip() for i in f.readlines()]

Slope = namedtuple('Slope', ['x', 'y'])

slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]

def expand_map(world_map, slope):
    full_map = []
    height = len(world_map)
    width = len(world_map[0])
    req_width = ((slope.x / slope.y) * height)
    exp_factor = int(math.ceil(req_width / width))
    for row in world_map:
        full_map.append(row * exp_factor)
    return full_map

def locate_trees(full_map):
    trees = set()
    for y, row in enumerate(full_map):
        for x, tile in enumerate(row):
            if tile == '#':
                trees.add((x, y))
    return trees

def traverse_map(trees, slope):
    height = len(full_map)
    width = len(full_map[0])
    x = 0
    y = 0
    tree_count = 0
    while y <= height:
        x += slope.x
        y += slope.y
        if (x, y) in trees:
            tree_count += 1
    return tree_count

tree_counts = []
for slope in slopes:
    full_map = expand_map(world_map, slope)
    trees = locate_trees(full_map)
    tree_count = traverse_map(trees, slope)
    tree_counts.append(tree_count)

solution = math.prod(tree_counts)
print(solution)