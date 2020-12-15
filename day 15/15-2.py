import collections

with open('input') as f:
    numbers = [int(x) for x in f.read().split(',')[:-1]]

numberdict = collections.defaultdict(int, {v:k+1 for k,v in enumerate(numbers)})
timestep = 6
current = 0
while timestep < 30000000:
    lasttime = numberdict[current]
    numberdict[current] = timestep
    current = (timestep - lasttime) % timestep
    timestep += 1

print(current)