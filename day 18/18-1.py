with open('input') as f:
    equations = [x.replace('(', '( ').replace(')', ' )').split(' ') for x in f.read().splitlines()]

def fix_equation(equation):

    def add_parens(equation, left, current):
        equation.insert(left, '(')
        equation.insert(current+2, ')')
        return equation

    current = 0
    left = 0
    left_queue = []
    while current < len(equation):
        if equation[current] == '(':
            left_queue.append(left)
            left = current+1
        elif equation[current] in '0123456789':
            equation = add_parens(equation, left, current)
            current += 2
        elif equation[current] == ')':
            left = left_queue.pop()
            equation = add_parens(equation, left, current)
            current += 2
        current += 1

    return equation

total = 0
for equation in equations:
    equation = fix_equation(equation)
    fixed = ''.join(equation)
    total += eval(fixed)

print(total)
