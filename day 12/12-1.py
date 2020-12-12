import re

with open('input') as f:
    instructions = f.read().splitlines()

directions = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
}

facings = {
    0  : directions['N'],
    90 : directions['E'],
    180: directions['S'],
    270: directions['W'],
}

x = 0
y = 0
facing = 90
for instruction in instructions:
    parsed = re.match('(\w)(\d+)', instruction)
    if parsed[1] in 'NESW':
        x += (directions[parsed[1]][0] * int(parsed[2]))
        y += (directions[parsed[1]][1] * int(parsed[2]))
    elif parsed[1] == 'F':
        x += (facings[facing][0] * int(parsed[2]))
        y += (facings[facing][1] * int(parsed[2]))
    elif parsed[1] == 'L':
        facing -= int(parsed[2])
    elif parsed[1] == 'R':
        facing += int(parsed[2])
    facing = facing % 360

dist = abs(x) + abs(y)
print(dist)