import re

with open('input') as f:
    data = f.read().splitlines()

def set_bit(value, index):
    value = value | (1 << index)
    return value

def unset_bit(value, index):
    value = value & ~(1 << index)
    return value

def apply_mask(mask, address, index):
    addresses = []
    for i in range(index, len(mask)):
        if mask[i] == '1':
            address = set_bit(address, i)
        elif mask[i] == 'X':
            addresses.extend(apply_mask(mask, set_bit(address, i), i+1))
            addresses.extend(apply_mask(mask, unset_bit(address, i), i+1))
            return addresses
    addresses.append(address)
    return addresses

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
        addresses = apply_mask(mask, address, 0)
        for address in addresses:
            memory[address] = value

print(sum(memory.values()))