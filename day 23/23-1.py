cups = [int(x) for x in list('167248359')]
current_i = 0
for _ in range(100):
    current_v = cups[current_i]
    move = [cups[(current_i+i) % len(cups)] for i in (1, 2, 3)]
    new_v = current_v - 1
    while new_v in move+[0]:
        new_v -= 1
        if new_v <= 0: new_v = 9
    for x in move:
        cups.remove(x)
    next_v = cups[(cups.index(current_v)+1) % len(cups)]
    new_i = cups.index(new_v)
    try:
        for x in reversed(move):
            cups.insert(new_i+1, x)
    except IndexError: cups.extend(move)
    current_i = cups.index(next_v)

solution = cups[cups.index(1)+1:]+cups[:cups.index(1)]
print(''.join(str(x) for x in solution))