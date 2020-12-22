file = open("day3_input.txt", "r")
lines = file.readlines()
file.close()

x = 0
max_x = len(lines[0])-1
trees = 0

for y in range(1,len(lines)):
	x = (x+3)%max_x
	if lines[y][x]=='#':
		trees += 1
		
print(trees)

#part 2
d = [(1,1), (3,1), (5,1), (7,1), (1,2)]
dtrees = []
for (dx, dy) in d:
	x = 0
	max_x = len(lines[0])-1
	trees = 0

	for y in range(dy,len(lines),dy):
		x = (x+dx)%max_x
		if lines[y][x]=='#':
			trees += 1
	
	dtrees.append(trees)
	

i = 1
for j in dtrees:
	i*=j
print(dtrees,i)
