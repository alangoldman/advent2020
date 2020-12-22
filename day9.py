file = open("day9_input.txt", "r")
nums = [int(l.rstrip()) for l in file.readlines()]
file.close()

p_len = 25

preamble = nums[0:p_len]
dict_preamble = {}
for i in preamble:
	if i in dict_preamble:
		dict_preamble[i] += 1
	else:
		dict_preamble[i] = 1


def is_valid(num):
	for i in preamble:
		if num-i in dict_preamble:
			if num-i == i:
				if dict_preamble[i] > 1:
					return True
				else:
					continue
			return True
	return False

for i in range(p_len, len(nums)):
	if not is_valid(nums[i]):
		invalid_num = nums[i]
		print(i, nums[i])
		break

	last_num = preamble.pop(0)
	dict_preamble[last_num]-=1
	if dict_preamble[last_num] == 0:
		del dict_preamble[last_num]

	preamble.append(nums[i])
	if nums[i] in dict_preamble:
		dict_preamble[nums[i]] += 1
	else:
		dict_preamble[nums[i]] = 1
	
done = False
for i in range(0,len(nums)-1):
	for j in range(i+2,len(nums)):
		if sum(nums[i:j]) == invalid_num:
			done = True
			smallest = min(nums[i:j])
			largest = max(nums[i:j])
			print(smallest, largest, smallest+largest)
			break
	if done:
		break