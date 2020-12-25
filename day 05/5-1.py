with open('input') as f:
    codes = f.read().splitlines()

highest = 0
for code in codes:
    row = code[:7]
    column = code[7:]
    row = row.replace('F', '0').replace('B', '1')
    column = column.replace('L', '0').replace('R', '1')
    row = int(row, 2)
    column = int(column, 2)
    seat_id = (row * 8) + column
    if seat_id > highest:
        highest = seat_id

print(highest)