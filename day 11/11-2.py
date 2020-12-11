import functools
import collections

with open('input') as f:
    grid = f.read().splitlines()

def parse_grid(grid):
    empty = set()
    occupied = set()
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == 'L':
                empty.add((x,y))

    return empty, occupied

def num_visible(seat, empty, occupied, constraints):
    total = 0

    #right
    x, y = seat[0], seat[1]
    while x <= constraints['max_x']:
        x += 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    #left
    x, y = seat[0], seat[1]
    while x >= constraints['min_x']:
        x -= 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    #up
    x, y = seat[0], seat[1]
    while y >= constraints['min_y']:
        y -= 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    #down
    x, y = seat[0], seat[1]
    while y <= constraints['max_y']:
        y += 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    #up-right
    x, y = seat[0], seat[1]
    while x <= constraints['max_x'] and y >= constraints['min_y']:
        x += 1
        y -= 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    #down-right
    x, y = seat[0], seat[1]
    while x <= constraints['max_x'] and y <= constraints['max_y']:
        x += 1
        y += 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    #up-left
    x, y = seat[0], seat[1]
    while x >= constraints['min_x'] and y >= constraints['min_y']:
        x -= 1
        y -= 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    #down-left
    x, y = seat[0], seat[1]
    while x >= constraints['min_x'] and y <= constraints['max_y']:
        x -= 1
        y += 1
        if (x, y) in occupied:
            total += 1
            break
        elif (x, y) in empty:
            break

    return total

def timestep(empty, occupied):
    new_empty = set(empty)
    new_occupied = set(occupied)
    constraints = collections.defaultdict(int)
    for seat in occupied:
        constraints['max_x'] = max(constraints['max_x'], seat[0])
        constraints['max_y'] = max(constraints['max_x'], seat[1])
        constraints['min_x'] = min(constraints['min_x'], seat[0])
        constraints['min_y'] = min(constraints['min_x'], seat[1])

    for seat in empty:
        if num_visible(seat, empty, occupied, constraints) == 0:
            new_occupied.add(seat)
            new_empty.remove(seat)
    for seat in occupied:
        if num_visible(seat, empty, occupied, constraints) >= 5:
            new_empty.add(seat)
            new_occupied.remove(seat)

    return new_empty, new_occupied

empty, occupied = parse_grid(grid)

while True:
    print(len(occupied), len(empty))
    new_empty, new_occupied = timestep(empty, occupied)
    if new_empty == empty:
        break
    empty = set(new_empty)
    occupied = set(new_occupied)
