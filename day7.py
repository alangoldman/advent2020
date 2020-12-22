file = open("day7_input.txt", "r")
rules = [l.rstrip() for l in file.readlines()]
file.close()

target = 'shiny gold'
mapping = {}
contents = {}
total_in_bags = {}
for rule in rules:
	outside_color = rule.split('bags')[0].rstrip()
	rule = rule.split('contain')[1]
	if rule == ' no other bags.':
		total_in_bags[outside_color] = 1
		continue
	
	contents[outside_color] = []
	colors = rule.split(',')
	for color in colors:
		inside_color = color.strip(' .')
		number = int(inside_color.split(' ')[0])
		inside_color = color.strip('0123456789 .').replace(' bags','').replace(' bag','')
		contents[outside_color].append((number, inside_color))
		if inside_color not in mapping:
			mapping[inside_color] = set([outside_color])
		else:
			mapping[inside_color].add(outside_color)
			
total = 0
stack = [target]
seen = set()
while len(stack) > 0:
	color = stack.pop()
	if color not in mapping:
		continue
	for outside_color in mapping[color]:
		if outside_color in seen:
			continue
		seen.add(outside_color)
		total += 1
		stack.append(outside_color)

print(total)

base_colors = set([color for color in total_in_bags.keys() if total_in_bags[color]==1])
#part 2
def find_total_in_bags(outside_color):
	if outside_color in total_in_bags:
		return total_in_bags[outside_color] #memoize
	total = 0
	for (num, color) in contents[outside_color]:
		total += num*find_total_in_bags(color)
		if color not in base_colors:
			total += num

	total_in_bags[outside_color] = total
	return total
	
find_total_in_bags(target)