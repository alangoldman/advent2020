#input = 389125467
input = 135468729

cups = []
while input > 0:
    cups.append(input % 10)
    input = int(input/10)

cups.reverse()
all_cups = cups.copy()

current_cup = 0


def move(current_cup):
    current_start = cups[current_cup]
    destination = cups[current_cup] - 1

    pickup_location = (current_cup + 1) % len(cups)

    pickup = []
    for i in range(3):
        if pickup_location >= len(cups):
            pickup_location = 0
        pickup.append(cups.pop(pickup_location))
    pickup.reverse()

    if destination < min(all_cups):
        destination = max(all_cups)
    while destination in pickup:
        destination -= 1
        if destination < min(all_cups):
            destination = max(all_cups)

    destination_idx = cups.index(destination)
    #if destination_idx == 0:
        #destination_idx = len(cups)
    insert_location = destination_idx + 1
    for c in pickup:
        cups.insert(insert_location, c)

    current_cup = cups.index(current_start)
    return (current_cup + 1) % len(cups)


for i in range(1, 100+1):
    current_cup = move(current_cup)

p = cups.index(1) + 1
result = ''
for i in range(len(cups)-1):
    p %= len(cups)
    result += str(cups[p])
    p += 1
print(result)