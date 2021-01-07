#input = 389125467
input = 135468729
part2 = True


class Node:
    def __init__(self, num, next_node=None):
        self.data = num
        self.next = next_node

    def __repr__(self):
        return str(self.data) + ' -> ' + (str(self.next.data) if self.next is not None else 'None')

    def print(self, comma=True):
        result = ''
        seen = set()
        head = self
        while head.data not in seen:
            seen.add(head.data)
            result += str(head.data)
            if comma:
                result += ', '
            head = head.next
        return result


all_cups = []
while input > 0:
    cur = input % 10
    all_cups.append(cur)
    input = int(input / 10)

all_cups.reverse()
if part2:
    for i in range(max(all_cups) + 1, 1000000 + 1):
        all_cups.append(i)
all_cups.reverse()

lookup = {}
head = None
last = None
cups_min = None
cups_max = None
for cup in all_cups:
    n = Node(cup, head)
    lookup[cup] = n
    head = n
    if last is None:
        last = n

    if cups_min is None or cup < cups_min:
        cups_min = cup
    if cups_max is None or cup > cups_max:
        cups_max = cup

last.next = head
current_cup = head


def move(current_cup):
    current_start = current_cup.data
    destination_num = current_start - 1

    pickup = current_cup.next
    pickup_seen = set([pickup.data, pickup.next.data, pickup.next.next.data])
    current_cup.next = current_cup.next.next.next.next

    if destination_num < cups_min:
        destination_num = cups_max
    while destination_num in pickup_seen:
        destination_num -= 1
        if destination_num < cups_min:
            destination_num = cups_max

    destination = lookup[destination_num]
    pickup.next.next.next = destination.next
    destination.next = pickup

    return current_cup.next


moves = 100 if not part2 else 10000000
for i in range(1, moves + 1):
    current_cup = move(current_cup)

p = lookup[1].next
if part2:
    a = p.data
    b = p.next.data
    print(a, b, a*b)
else:
    print(p.print(comma=False)[:-1])
