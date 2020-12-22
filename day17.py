file = open("day17_input.example.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

x = 0
max_x = len(lines[0])-1

for y in range(0,len(lines)):
	if lines[y][x] == '#'