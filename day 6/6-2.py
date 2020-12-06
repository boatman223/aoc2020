with open('input') as f:
    groups = [i.split('\n') for i in f.read().split('\n\n')]

total = 0
for group in groups:
    answers = [set(i) for i in group]
    intersection = answers[0].intersection(*answers[1:])
    total += len(intersection)

print(total)