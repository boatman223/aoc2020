import itertools

with open('input') as f:
    numbers = [int(x) for x in f.read().splitlines()]

index = 0
for i, number in enumerate(numbers):
    pairs = itertools.permutations(numbers[i:i+25], 2)
    for pair in pairs:
        if pair[0] + pair[1] == numbers[i+25]:
            break
    else:
        vuln = numbers[i+25]
        break
    i += 1