import re

with open('input') as f:
    data = f.read().splitlines()

def set_bit(value, index):
    value = value | (1 << index)
    return value

def unset_bit(value, index):
    value = value & ~(1 << index)
    return value

memory = {}
mask = ''
pattern = re.compile('(mask|mem)(\[(\d+)\])? = (.+)')
for line in data:
    match = pattern.match(line)
    instruction = match[1]
    address = match[3]
    try: value = int(match[4])
    except ValueError: value = match[4]
    if instruction == 'mask':
        mask = value
    elif instruction == 'mem':
        for i, bit in enumerate(reversed(mask)):
            if bit == '1':
                value = set_bit(value, i)
            elif bit == '0':
                value = unset_bit(value, i)
        memory[address] = value

print(sum(memory.values()))