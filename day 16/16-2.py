import re

with open('input') as f:
    data = f.read().split('\n\n')

def remove_invalid_tickets(tickets, rules):
    all_valid_numbers = set()
    for x in rules.values():
        all_valid_numbers.update(x)

    for ticket in tickets[:]:
        for value in ticket:
            if value not in all_valid_numbers:
                tickets.remove(ticket)
                break

    return tickets

def parse_data(data):
    PATTERN = re.compile('([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)')
    rules = {}
    for line in data[0].splitlines():
        match = PATTERN.match(line)
        x = set()
        x.update(range(int(match[2]), int(match[3])+1))
        x.update(range(int(match[4]), int(match[5])+1))
        rules[match[1]] = x

    tickets = []
    for line in data[2].splitlines()[1:]:
        tickets.append([int(x) for x in line.split(',')])
    tickets = remove_invalid_tickets(tickets, rules)

    my_ticket = [int(x) for x in data[1].splitlines()[1].split(',')]

    fields = [[] for _ in range(len(tickets[0]))]
    for ticket in tickets:
        for i, value in enumerate(ticket):
            fields[i].append(value)

    valid_fields = [list(rules.keys()) for _ in range(len(fields))]

    return rules, my_ticket, fields, valid_fields

def check_field_validity(fields, rules, valid_fields):
    for i, field in enumerate(fields):
        for value in field:
            for field_name, valid_numbers in rules.items():
                if value not in valid_numbers:
                    try: valid_fields[i].remove(field_name)
                    except ValueError: pass

    return valid_fields

def pare_valid_fields(valid_fields):
    valid_fields2 = [[] for _ in range(len(valid_fields))]
    while True:
        for i, x in enumerate(valid_fields[:]):
            if len(x) == 1:
                valid_fields2[i] = x
                valid_fields[i] = []
                for y in valid_fields:
                    try: y.remove(x[0])
                    except ValueError: pass
                break
        else: break

    return valid_fields2

def compute_solution(valid_fields, my_ticket):
    total = 1
    for i, field in enumerate(valid_fields):
        if field[0].startswith('departure'):
            total *= my_ticket[i]

    return total

rules, my_ticket, fields, valid_fields = parse_data(data)
valid_fields = check_field_validity(fields, rules, valid_fields)
valid_fields = pare_valid_fields(valid_fields)
solution = compute_solution(valid_fields, my_ticket)

print(solution)