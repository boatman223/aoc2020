import collections

with open('input') as f:
    data = [int(x) for x in f.read().split(',')]

timestep = len(data)
current = data[-1]
numbers = collections.defaultdict(int, {v:k+1 for k,v in enumerate(data[:-1])})

while timestep < 30000000:
    lasttime = numbers[current]
    numbers[current] = timestep
    current = (timestep - lasttime) % timestep
    timestep += 1

print(current)