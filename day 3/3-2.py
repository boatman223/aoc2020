from collections import namedtuple
import math

with open('input') as f:
    world_map = [i.strip() for i in f.readlines()]

Slope = namedtuple('Slope', ['x', 'y'])

slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]

def locate_trees(world_map):
    trees = set()
    for y, row in enumerate(world_map):
        for x, tile in enumerate(row):
            if tile == '#':
                trees.add((x, y))
    return trees

def traverse_map(trees, slope):
    height = len(world_map)
    width = len(world_map[0])
    x = 0
    y = 0
    tree_count = 0
    while y <= height:
        x = (x + slope.x) % width
        y += slope.y
        if (x, y) in trees:
            tree_count += 1
    return tree_count

tree_counts = []
for slope in slopes:
    trees = locate_trees(world_map)
    tree_count = traverse_map(trees, slope)
    tree_counts.append(tree_count)

solution = math.prod(tree_counts)
print(solution)