import itertools

with open('input') as f:
    grid = f.read().splitlines()

def parse_input(grid):
    active = set()
    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == '#':
                active.add((x, y, 0))

    return active

def get_adjacent_cells(x, y, z):
    directions = list(itertools.product((-1, 0, 1), repeat=3))
    directions.remove((0, 0, 0))
    cells = set()
    for x2, y2, z2 in directions:
        cells.add((x+x2, y+y2, z+z2))

    return cells

def timestep(active):
    new_active = set()
    inactive = set()
    for x, y, z in active:
        adjacent = get_adjacent_cells(x, y, z)
        inactive.update({cell for cell in adjacent if cell not in active})
        active_adjacent = {cell for cell in adjacent if cell in active}
        if len(active_adjacent) in (2, 3):
            new_active.add((x, y, z))
    for x, y, z in inactive:
        adjacent = get_adjacent_cells(x, y, z)
        active_adjacent = {cell for cell in adjacent if cell in active}
        if len(active_adjacent) == 3:
            new_active.add((x, y, z))

    return new_active

active = parse_input(grid)
for i in range(6):
    active = timestep(active)

print(len(active))