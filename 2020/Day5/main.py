import math
with open('input.txt') as reader:
    data = reader.readlines()

data = [x.rstrip() for x in data]

def get_row(letters):
    row = [0,127]
    for i in letters:
        if(i == 'F'):
            row[1] = math.floor((row[0]+row[1])/2)
        else:
            row[0] = math.ceil((row[0]+row[1])/2)
        #print(row)
    return row[0]
def get_col(letters):
    col = [0,7]
    for i in letters:
        if(i == 'R'):
            col[0] = math.ceil((col[0]+col[1])/2)
        else:
            col[1] = math.floor((col[0]+col[1])/2)
    #print(col)
    return col[0]
def get_seat(row,col):
    return row*8 + col
# <------------PART 1 ---------->
high = 0
low = 10000
for bp in data:
    r = get_row(bp[:-3])
    c = get_col(bp[-3:])
    seat = get_seat(r,c)
    high = seat if seat > high else high
    low = seat if seat < low else low

print(f'HIGH = {high} \t LOW={low}')
# < ----------PART 2 ----------->
seats=[]
for bp in data:
    r = get_row(bp[:-3])
    c = get_col(bp[-3:])
    seats.append(get_seat(r,c))
my_seat = []
max_min = [high,low]
for seat in seats:
    if (seat + 1) not in seats:
        if seat not in max_min:
            my_seat.append(seat)
    if (seat - 1) not in seats:
        if seat not in max_min:
            my_seat.append(seat)
my_seat.sort()
print(f'MY SEAT = {my_seat[0] + (my_seat[1] - my_seat[0]) - 1}')
