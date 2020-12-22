file = open("day2_input.txt", "r")
lines = file.readlines()
file.close()

data = [s.split(' ') for s in lines]
valid = 0
for (policy, letter, password) in data:
	count = password.count(letter[0])
	min, max = policy.split('-')
	min = int(min)
	max = int(max)
	if min <= count <= max:
		valid += 1

print(valid)

#part 2
valid = 0
for (policy, letter, password) in data:
	pos1, pos2 = policy.split('-')
	pos1 = int(pos1)
	pos2 = int(pos2)
	if (password[pos1-1]==letter[0]) ^ (password[pos2-1]==letter[0]):
		valid += 1
		
print(valid)