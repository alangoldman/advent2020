nums = '6,19,0,5,7,13,1'
#nums = '0,3,6'
nums = [int(i) for i in nums.split(',')]

spoken = {}
last_spoken = -1
last_spoken_first = False

def speak(num, turn):
    last_spoken_first = False
    if num not in spoken:
        spoken[num] = [turn]
        last_spoken_first = True
    else:
        spoken[num].append(turn)
    last_spoken = num
    return spoken, last_spoken, last_spoken_first
    
turn = 1
for num in nums:
    spoken, last_spoken, last_spoken_first = speak(num, turn)
    turn += 1

while turn <= 30000000:
    if last_spoken_first:
        spoken, last_spoken, last_spoken_first = speak(0, turn)
    else:
        spoken, last_spoken, last_spoken_first = speak(turn-1-spoken[last_spoken][-2], turn)
    turn += 1

print(last_spoken)