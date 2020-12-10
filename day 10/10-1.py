import collections

with open('input') as f:
    adapters = [int(x) for x in f.read().splitlines()]

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

diffs = collections.defaultdict(int)
for i, adapter in enumerate(adapters):
    try:
        diff = adapter - adapters[i+1]
        diffs[diff] += 1
    except IndexError:
        break

solution = diffs[-1] * diffs[-3]

print(solution)