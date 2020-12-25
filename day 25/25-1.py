def do_loop(subject_number, value):
    value *= subject_number
    value = value % 20201227
    return value

def get_encryption_key(loops, subject_number):
    value = 1
    for _ in range(loops):
        value = do_loop(subject_number, value)
    return value

with open('input') as f:
    card_key, door_key = (int(x) for x in f.read().splitlines())

subject_number = 7
value = 1
card_loops = 0
while value != card_key:
    value = do_loop(subject_number, value)
    card_loops += 1

print(get_encryption_key(card_loops, door_key))