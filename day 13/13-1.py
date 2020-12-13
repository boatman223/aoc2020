import re

with open('input') as f:
    data = f.read().splitlines()

timestamp = int(data[0])
buses = [int(x) for x in re.findall('(\d+)', data[1])]

arrivals = {}
for bus in buses:
    arrivals[bus] = (bus - (timestamp % bus))

soonest_id = min(arrivals, key=arrivals.get)

solution = arrivals[soonest_id] * soonest_id
print(solution)