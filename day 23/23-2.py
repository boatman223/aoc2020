def loopdown(n):
    if n == 0: return 1_000_000
    return n

data = [int(x) for x in list('167248359')] + list(range(10, 1_000_001))
cups = {cup:data[(i+1)%1_000_000] for i, cup in enumerate(data)}

current_i = 1
for _ in range(10_000_000):
    move1 = cups[current_i]
    move2 = cups[move1]
    move3 = cups[move2]
    next_i = cups[move3]
    move_to = loopdown(current_i-1)
    while move_to in (move1, move2, move3):
        move_to = loopdown(move_to-1)
    cups[current_i] = next_i
    cups[move3] = cups[move_to]
    cups[move_to] = move1
    current_i = next_i

print(cups[1]*cups[cups[1]])