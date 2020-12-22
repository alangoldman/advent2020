import string
file = open("day6_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

groups = []
group = ''
for l in lines:
	l = l.rstrip()
	if l == '' and group:
		groups.append(group)
		group = ''
	else:
		group += l+' '
		
if group != '':
	groups.append(group)
	
total = 0
for group in groups:
	people = group.split(' ')
	all_answers = None
	for person in people:
		if person == '':
			continue
		answers = set()
		for c in person:
			if c != ' ':
				answers.add(c)
		if all_answers is None:
			all_answers = answers
		else:
			all_answers = all_answers.intersection(answers)
	total += len(all_answers)
	
print(total)

#part 2