def build_passports(data):
    passports = []
    for passport in data:
        passdict = {}
        passport = passport.replace('\n', ' ').split(' ')
        for field in passport:
            k, v = field.split(':')
            passdict[k] = v
        passports.append(passdict)
    return passports

def is_valid(passport, req_fields):
    fields = set(list(passport))
    if not fields.issuperset(req_fields):
        return False

    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False

    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False

    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    if passport['hgt'][-2:] == 'cm':
        if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
            return False
    else:
        return False

    if passport['hcl'][0] != '#':
        return False
    if len(passport['hcl']) != 7:
        return False
    for char in passport['hcl'][1:]:
        if char.lower() not in '0123456789abcdef':
            return False

    if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    if not passport['pid'].isnumeric():
        return False
    if len(passport['pid']) != 9:
        return False

    return True

req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

with open('input') as f:
    data = f.read().split('\n\n')

passports = build_passports(data)
valid_passports = 0
for passport in passports:
    if is_valid(passport, req_fields):
        valid_passports += 1
print(valid_passports)