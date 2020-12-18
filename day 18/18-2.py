import collections

with open('input') as f:
    equations = [x.replace('(', '( ').replace(')', ' )').split(' ') for x in f.read().splitlines()]

def fix_equation(equation):
    current = 0
    matching_left = 0
    left_queue = []
    add_right = collections.defaultdict(lambda: False)
    while current < len(equation):
        if equation[current] == '(':
            left_queue.append(current)

        elif equation[current] == ')':
            matching_left = left_queue.pop()
            if add_right[len(left_queue)]:
                equation.insert(current, ')')
                add_right[len(left_queue)] = False
                current += 1

        elif equation[current] == '+':
            if equation[current-1] in '0123456789':
                equation.insert(current-1, '(')
                matching_left = current-1
                current += 1
            elif equation[current-1] == ')':
                equation.insert(matching_left, '(')
                current += 1

            if equation[current+1] in '0123456789':
                equation.insert(current+2, ')')
                current += 2
            elif equation[current+1] == '(':
                add_right[len(left_queue)] = True

        current += 1

    return equation

total = 0
for equation in equations:
    equation = fix_equation(equation)
    fixed = ''.join(equation)
    total += eval(fixed)

print(total)
