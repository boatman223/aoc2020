import re

with open('input') as f:
    instructions = f.read().splitlines()

directions = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}

rotations = {
    'L': (1, -1),
    'R': (-1, 1),
}

ship = {'x': 0, 'y': 0}
waypoint = {'x': 10, 'y': 1}

for instruction in instructions:
    print(ship, waypoint, instruction)
    parsed = re.match('(\w)(\d+)', instruction)
    letter = parsed[1]
    amount = int(parsed[2])
    if letter in 'NESW':
        waypoint['x'] += (directions[letter][0] * amount)
        waypoint['y'] += (directions[letter][1] * amount)
    elif letter in 'LR':
        for _ in range(amount//90):
            new_x = waypoint['y'] * rotations[letter][1]
            new_y = waypoint['x'] * rotations[letter][0]
            waypoint['x'] = new_x
            waypoint['y'] = new_y
    elif letter == 'F':
        ship['x'] += (waypoint['x'] * amount)
        ship['y'] += (waypoint['y'] * amount)

dist = abs(ship['x']) + abs(ship['y'])
print(dist)