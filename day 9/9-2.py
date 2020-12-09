import itertools

with open('input') as f:
    numbers = [int(x) for x in f.read().splitlines()]

index = 0
vuln = 0
for i, number in enumerate(numbers):
    pairs = itertools.permutations(numbers[i:i+25], 2)
    for pair in pairs:
        if pair[0] + pair[1] == numbers[i+25]:
            break
    else:
        vuln = numbers[i+25]
        break
    i += 1

index = 0
weakness = []
while sum(weakness) != vuln:
    while sum(weakness) < vuln:
        weakness.append(numbers[index])
        index += 1
    while sum(weakness) > vuln:
        weakness.pop(0)

weakness = max(weakness) + min(weakness)
print(weakness)