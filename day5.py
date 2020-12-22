file = open("day5_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

max_seat_id = 0
seat_ids = set()
for seat in lines:
	row = seat[0:7]
	column = seat[7:10]
	b_row = ''.join(['0' if c =='F' else '1' for c in row])
	b_col = ''.join(['0' if c =='L' else '1' for c in column])
	d_row = int(b_row,2)
	d_col = int(b_col,2)
	seat_id = d_row*8 + d_col
	seat_ids.add(seat_id)
	max_seat_id = max(max_seat_id, seat_id)
	
print(max_seat_id)

#part 2

for i in range(0,max_seat_id):
	if i not in seat_ids:
		print(i) # use the last one