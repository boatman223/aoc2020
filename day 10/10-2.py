import collections

with open('input') as f:
    adapters = [int(x) for x in f.read().splitlines()]

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1]+3)

optional = 0
req1 = 0
prev = 0
for i, adapter in enumerate(adapters):
    if adapters[i] - adapters[i-1] == 3:
        if i - prev == 5:
            req1 += 1
        elif i - prev == 4:
            optional += 2
        elif i - prev == 3:
            optional += 1
        prev = i

total = 2**(req1*3 + optional)
for i in range(req1):
    total -= (2**(req1 * 3 + optional- ((i+1)*3)) * (7**i))

print(total)