file = open("day22_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

deck1 = []
deck2 = []
player1 = False
for line in lines:
    if 'Player' in line:
        player1 = not player1
    elif line == '':
        continue
    elif player1:
        deck1.append(int(line))
    else:
        deck2.append(int(line))

seen = set()
while not (len(deck1) == 0 or len(deck2) == 0):
    p1 = deck1.pop(0)
    p2 = deck2.pop(0)
    if (p1, p2) in seen:
        winning_deck = deck1
        #break

    seen.add((p1, p2))
    if p1 > p2:
        deck1.append(p1)
        deck1.append(p2)
    else:
        deck2.append(p2)
        deck2.append(p1)

if len(deck1) == 0:
    winning_deck = deck2
elif len(deck2) == 0:
    winning_deck = deck1

score = 0
for i in range(len(winning_deck)):
    score += winning_deck[i] * (len(winning_deck)-i)
print(score)