file = open("day21_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

foods = []
all_contents = set()
all_allergens = set()
allergen_map = {}
ingrediant_map = {}

for line in lines:
    contents, allergens = line.split(' (')
    contents = contents.split(' ')
    allergens = allergens[9:-1].split(', ')

    foods.append((set(contents), set(allergens)))
    all_contents = all_contents.union(contents)
    all_allergens = all_allergens.union(allergens)

while len(allergen_map.keys()) != len(all_allergens):
    for allergen in all_allergens:
        possible_ingredients = all_contents.difference(set(allergen_map.values()))
        for food in foods:
            if allergen in food[1]:
                possible_ingredients = possible_ingredients.intersection(food[0])
        if len(possible_ingredients) == 1:
            allergen_map[allergen] = possible_ingredients.pop()
        #print(allergen, possible_ingredients)

total = 0
for ingredient in all_contents:
    if ingredient not in allergen_map.values():
        for food in foods:
            if ingredient in food[0]:
                total += 1
print(total)

# part 2
dangerous = []
for allergen in sorted(allergen_map.keys()):
    dangerous.append(allergen_map[allergen])
print(','.join(dangerous))