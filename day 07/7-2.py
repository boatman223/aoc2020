import re

with open('input') as f:
    data = f.read().splitlines()

def parse_bags(data):
    bagdict = {}
    for line in data:
        outside = ' '.join(line.split()[:2])
        inside = re.findall('(\d) ([a-z]+ [a-z]+)', line)
        bagdict[outside] = inside

    return bagdict

def outside_in(total, target):
    for bag in bagdict[target]:
        total += int(bag[0])
        total += int(bag[0]) * outside_in(0, bag[1])

    return total

bagdict = parse_bags(data)
total = outside_in(0, 'shiny gold')

print(total)
