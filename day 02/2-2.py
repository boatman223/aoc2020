with open('input', 'r') as f:
    passwords = [i.strip().split() for i in f.readlines()]

valid_passwords = []
for entry in passwords:
    pos1 = int(entry[0].split('-')[0]) - 1
    pos2 = int(entry[0].split('-')[1]) - 1
    letter = entry[1][0]
    password = entry[2]
    if (password[pos1] == letter) ^ (password[pos2] == letter):
        valid_passwords.append(password)

solution = len(valid_passwords)
print(solution)