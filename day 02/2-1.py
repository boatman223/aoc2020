with open('input', 'r') as f:
    passwords = [i.strip().split() for i in f.readlines()]

valid_passwords = []
for entry in passwords:
    minimum = int(entry[0].split('-')[0])
    maximum = int(entry[0].split('-')[1])
    letter_count = entry[2].count(entry[1][0])
    password = entry[2]
    if letter_count >= minimum and letter_count <= maximum:
        valid_passwords.append(password)

solution = len(valid_passwords)
print(solution)