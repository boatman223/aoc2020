import re

with open('input') as f:
    rules, messages = f.read().split('\n\n')

messages = messages.splitlines()
rules = [x.split(':') for x in rules.split('\n')]
ruledict = {k:v[1:].replace('"', '') for k,v in rules}

PATTERN = re.compile('\d+')
def find_valid_messages(rule):
    rightadj = 0
    for match in re.finditer(PATTERN, rule):
        if '|' not in ruledict[match[0]]:
            rule = rule[:match.start()+rightadj] + ruledict[match[0]] + rule[match.end()+rightadj:]
            rightadj += len(ruledict[match[0]]) - len(match[0])
        else:
            b1, b2 = ruledict[match[0]].split('|')
            rule1 = rule[:match.start()+rightadj] + b1.strip() + rule[match.end()+rightadj:]
            rule2 = rule[:match.start()+rightadj] + b2.strip() + rule[match.end()+rightadj:]
            yield from find_valid_messages(rule1)
            yield from find_valid_messages(rule2)
            break
    else:
        if rule.replace(' ', '').isalpha():
            yield rule
        else:
            yield from find_valid_messages(rule)

valid_42 = set()
valid_31 = set()
for message in find_valid_messages('42'):
    valid_42.add(message.replace(' ', ''))

for message in find_valid_messages('31'):
    valid_31.add(message.replace(' ', ''))

# 0: 8 11
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# 42 and 31 are both length 8
# intersection of 42 and 31 is empty
# highest length message is 96
# possible sequences:
# 1-10 42s + 42 31
# 1-8 42s + 42 42 31 31
# 1-6 42s + 42 42 42 31 31 31
# 1-4 42s + 42 42 42 42 31 31 31 31
# 1-2 42s + 42 42 42 42 42 31 31 31 31 31

valid_messages = []
for i in range(1, 11):
    start = []
    start.extend([42]*i)
    for j in range(1, 6):
        full = start[:]
        full.extend([42]*j)
        full.extend([31]*j)
        if len(full) <= 12:
            valid_messages.append(full)

total = 0
for x in messages:
    parsed_message = []
    message = [x[i:i+8] for i in range(0, len(x), 8)]
    for block in message:
        if block in valid_42:
            parsed_message.append(42)
        elif block in valid_31:
            parsed_message.append(31)
        else: break
    else:
        if parsed_message in valid_messages:
            total += 1

print(total)