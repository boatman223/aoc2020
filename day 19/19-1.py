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

total = 0
for message in messages:
    if len(message) == 24:
        if message[0:8] in valid_42:
            if message[8:16] in valid_42:
                if message[16:24] in valid_31:
                    total += 1
print(total)