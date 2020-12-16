import re

with open('input') as f:
    data = f.read().split('\n\n')

rules = data[0]
ranges = (x.split('-') for x in re.findall('\d+-\d+', rules))
valid = set()
for lo, hi in ranges:
    valid.update(range(int(lo), int(hi)+1))

nearby = data[2]
numbers = (int(x) for x in re.findall('\d+', nearby))
total = 0
for number in numbers:
    if number not in valid:
        total += number

print(total)