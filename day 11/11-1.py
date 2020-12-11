import functools

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

def num_adjacent(seat, occupied):
    total = 0
    x = seat[0]
    y = seat[1]
    if (x, y+1) in occupied:
        total += 1
    if (x, y-1) in occupied:
        total += 1
    if (x+1, y) in occupied:
        total += 1
    if (x-1, y) in occupied:
        total += 1
    if (x+1, y+1) in occupied:
        total += 1
    if (x-1, y-1) in occupied:
        total += 1
    if (x-1, y+1) in occupied:
        total += 1
    if (x+1, y-1) in occupied:
        total += 1

    return total

def timestep(empty, occupied):
    new_empty = set(empty)
    new_occupied = set(occupied)
    for seat in (empty | occupied):
        if seat in empty and num_adjacent(seat, occupied) == 0:
            new_occupied.add(seat)
            new_empty.remove(seat)
        elif seat in occupied and num_adjacent(seat, occupied) >= 4:
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
