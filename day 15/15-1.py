with open('input') as f:
    numbers = [int(x) for x in f.read().split(',')]

time = len(numbers)-1
while time < 2019:
    current = numbers[time]
    next = time - numbers.index(current)
    numbers.append(next)
    if numbers.count(next) > 2:
        numbers[numbers.index(next)] = -1
    time += 1

print(numbers)