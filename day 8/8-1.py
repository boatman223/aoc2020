with open('input') as f:
    code = [i.split() for i in f.read().splitlines()]

index = 0
acc = 0
executed = []
while True:
    if index in executed:
        break
    executed.append(index)
    if code[index][0] == 'acc':
        acc += int(code[index][1])
    elif code[index][0] == 'jmp':
        index += int(code[index][1])
        continue
    index += 1

print(acc)