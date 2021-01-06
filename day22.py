file = open("day22_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

decks = [[], []]
player1 = False
for line in lines:
    if 'Player' in line:
        player1 = not player1
    elif line == '':
        continue
    elif player1:
        decks[0].append(int(line))
    else:
        decks[1].append(int(line))


def game(deck1, deck2):
    seen = set()
    while not (len(deck1) == 0 or len(deck2) == 0):
        state_hash = (tuple(deck1), tuple(deck2))
        if state_hash in seen:
            return 0, deck1
        seen.add(state_hash)

        p1 = deck1.pop(0)
        p2 = deck2.pop(0)

        if len(deck1) >= p1 and len(deck2) >= p2:
            winner, _ = game(deck1[:p1].copy(), deck2[:p2].copy())
            if winner == 0:
                deck1.append(p1)
                deck1.append(p2)
            else:
                deck2.append(p2)
                deck2.append(p1)
        else:
            if p1 > p2:
                deck1.append(p1)
                deck1.append(p2)
            else:
                deck2.append(p2)
                deck2.append(p1)

    if len(deck1) == 0:
        return 1, deck2
    elif len(deck2) == 0:
        return 0, deck1


winner, winning_deck = game(decks[0].copy(), decks[1].copy())
score = 0
for i in range(len(winning_deck)):
    score += winning_deck[i] * (len(winning_deck)-i)
print(score)