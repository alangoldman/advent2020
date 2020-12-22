file = open("C:/Users/alango/Downloads/input.txt", "r")
numbers = file.readlines()
file.close()

numbers = set([int(i) for i in numbers])

target = 2020

diff1 = [(i, target-i) for i in numbers]
for (x, y) in diff1:
	if x in numbers and y in numbers:
		print(x, y, x*y)

diff2 = [[(x, i, target-x-i) for (x, y) in diff1] for i in numbers]
for i in diff2:
	for (x,y,z) in i:
		if x in numbers and y in numbers and z in numbers:
			print(x,y,z,x*y*z)