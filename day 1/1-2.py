with open('input', 'r') as f:
    data = [int(i.strip()) for i in f.readlines()]

target = 2020

for i in data:
    for j in data:
        for k in data:
            if i + j + k == target:
                solution = i * j * k

print(solution)