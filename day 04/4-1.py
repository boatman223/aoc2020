with open('input') as f:
    data = f.read()
    passports = data.replace('\n\n', '!!!').replace('\n', ' ').replace('!!!', '\n').splitlines()

req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_passports = 0
for passport in passports:
    fields = set()
    passport = passport.split()
    for field in passport:
        fields.add(field.split(':')[0])
    if req_fields.issubset(fields):
        valid_passports += 1

print(valid_passports)
