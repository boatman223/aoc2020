import re

def build_passports(data):
    passports = []
    for passport in data:
        passport = passport.replace('\n', ' ').split(' ')
        passdict = dict(field.split(':') for field in passport)
        passports.append(passdict)

    return passports

def is_valid(passport, req_fields):
    fields = set(passport)
    if not fields >= req_fields:
        return False

    if not 1920 <= int(passport['byr']) <= 2002:
        return False

    if not 2010 <= int(passport['iyr']) <= 2020:
        return False

    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    if hgt := re.search('(\d+)(cm|in)', passport['hgt']):
        if hgt[2] == 'cm':
            if not 150 <= int(hgt[1]) <= 193:
                return False
        elif hgt[2] == 'in':
            if not 59 <= int(hgt[1]) <= 76:
                return False
    else:
        return False

    if not re.match('^#[0-9a-f]{6}$', passport['hcl']):
        return False

    if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    if not re.match('^\d{9}$', passport['pid']):
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