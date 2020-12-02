with open('input', 'r') as f:
    data = [int(i.strip()) for i in f.readlines()]

target = 2020

for i in data:
    for j in data:
        if i + j == target:
            solution = i * j

print(solution)