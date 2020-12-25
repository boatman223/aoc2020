with open('input') as f:
    groups = [i.replace('\n', '') for i in f.read().split('\n\n')]

total = 0
for group in groups:
    answers = set(group)
    total += len(answers)

print(total)