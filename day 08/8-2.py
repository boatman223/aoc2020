with open('input') as f:
    code = [i.split() for i in f.read().splitlines()]

def run_computer():
    index = 0
    acc = 0
    executed = []
    fixed = False
    while True:
        if index == len(code):
            fixed = True
            break
        if index in executed:
            break
        executed.append(index)
        if code[index][0] == 'acc':
            acc += int(code[index][1])
        elif code[index][0] == 'jmp':
            index += int(code[index][1])
            continue
        index += 1

    return acc, fixed

def swap_instruction(i, line):
    if line[0] == 'nop':
        code[i][0] = 'jmp'
    elif line[0] == 'jmp':
        code[i][0] = 'nop'
    return None

for i, line in enumerate(code[:]):
    swap_instruction(i, line)
    acc, fixed = run_computer()
    if fixed:
        break
    swap_instruction(i, line)

print(acc)
