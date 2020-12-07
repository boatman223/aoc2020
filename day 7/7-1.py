import re

with open('input') as f:
    data = f.read().splitlines()

def parse_bags(data):
    bagdict = {}
    for line in data:
        outside = ' '.join(line.split()[:2])
        inside = re.findall('\d ([a-z]+ [a-z]+)', line)
        bagdict[outside] = inside

    return bagdict

def inside_out(allbags, target):
    for k, v in bagdict.items():
        if target in v:
            allbags.add(k)
            allbags.update(inside_out(allbags, k))

    return allbags

bagdict = parse_bags(data)
allbags = inside_out(set(), 'shiny gold')

print(len(allbags))