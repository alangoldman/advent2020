file = open("day8_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

instructions = []
for line in lines:
	ist, num = line.split(' ')
	negative = num[0]=='-'
	num = int(num[1:]) * (-1 if negative else 1)
	instructions.append((ist, num))
	
	
def loops(ists):
	seen = set()
	acc = 0
	isp = 0
	last_isp = len(ists) - 1
	while isp not in seen and isp != last_isp:
		seen.add(isp)
		(ist, num) = ists[isp]
		if ist == 'acc':
			acc += num
			isp += 1
		if ist == 'jmp':
			isp += num
		if ist == 'nop':
			isp += 1
			
	return (isp in seen, acc)


print(loops(instructions)[1])
	
	
#part 2
225+56 * 611
#= 34441, let's brute force!


for i in range(0,len(instructions)):
	(prev_ist, num) = instructions[i]
	if instructions[i][0] == 'nop':
		instructions[i] = ('jmp', num)
	if instructions[i][0] == 'jmp':
		instructions[i] = ('nop', num)
	
	(loop, acc) = loops(instructions)
	if not loop:
		print(i, acc)
		
	instructions[i] = (prev_ist, num)
		