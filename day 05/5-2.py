with open('input') as f:
    codes = f.read().splitlines()

seats = []
for code in codes:
    row = code[:7]
    column = code[7:]
    row = row.replace('F', '0').replace('B', '1')
    column = column.replace('L', '0').replace('R', '1')
    row = int(row, 2)
    column = int(column, 2)
    seat_id = (row * 8) + column
    seats.append(seat_id)

seats.sort()
for i, seat in enumerate(seats):
    if (seats[i-1] + 1) != seats[i]:
        my_seat = seat - 1

print(my_seat)