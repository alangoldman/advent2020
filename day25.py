value = 1
subject_num = 7
loop_map = {}

for i in range(1, 10000000):
    value *= subject_num
    value %= 20201227
    loop_map[value] = i

#card_pub = 5764801
#door_pub = 17807724
card_pub = 335121
door_pub = 363891

card_loop = loop_map[card_pub]
door_loop = loop_map[door_pub]

value = 1
subject_num = card_pub
for i in range(door_loop):
    value *= subject_num
    value %= 20201227
    loop_map[value] = i

print(value)