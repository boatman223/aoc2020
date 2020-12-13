with open('input') as f:
    data = f.read().splitlines()[1].split(',')

busdict = {int(value):index%int(value) for index, value in enumerate(data) if value != 'x'}

addme = list(busdict.keys())[0]
timestamp = list(busdict.keys())[0]
for k, v in list(busdict.items())[1:]:
    first = 0
    while True:
        if timestamp % k == (k - v):
            if not first:
                first = timestamp
            else:
                addme = timestamp - first
                timestamp = first
                break
        timestamp += addme

print(first)