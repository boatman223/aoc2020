import re

def set_bit(value, index):
    return value | (1 << index)

def unset_bit(value, index):
    return value & ~(1 << index)

def apply_mask(mask, address, index):
    for i in range(index, len(mask)):
        if mask[i] == '1':
            address = set_bit(address, i)
        elif mask[i] == 'X':
            yield from apply_mask(mask, set_bit(address, i), i+1)
            yield from apply_mask(mask, unset_bit(address, i), i+1)
            break
    else:
        yield address


with open('input') as f:
    data = f.read().splitlines()

memory = {}
mask = ''
pattern = re.compile('(mask|mem)(\[(\d+)\])? = (.+)')
for line in data:
    match = pattern.match(line)
    instruction = match[1]
    if instruction == 'mask':
        mask = match[4][::-1]
    elif instruction == 'mem':
        address = int(match[3])
        value = int(match[4])
        for address in apply_mask(mask, address, 0):
            memory[address] = value

print(sum(memory.values()))