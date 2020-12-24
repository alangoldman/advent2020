file = open("day13_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

time = int(lines[0])
buses = lines[1]
buses = [int(x) if x!='x' else None for x in buses.split(',')]

best_id = -1
best_wait = -1
for bus in buses:
    if bus is None:
        continue
    missed = time%bus
    if missed == 0:
        wait = 0
    else:
        wait = bus - missed
    if best_wait == -1 or wait < best_wait:
        best_id = bus
        best_wait = wait
        
print(best_id, best_wait, best_id*best_wait)
        
# part 2

from math import gcd

def lcd(a, b):
    return int(a*b/gcd(a,b))

def verify(t, l=None):
    if l is None:
        l = len(buses)
    for i in range(0, l):
        if buses[i] is None:
            continue
        if (t+i)%buses[i] != 0:
            return False
            
    return True
        
        
    
multiple = buses[0]
t = buses[0]
for i in range(1, len(buses)):
    if buses[i] is None:
        continue

    while not verify(t, i+1):
        t += multiple
        
    multiple = lcd(multiple, buses[i])
    print(t, multiple)
    
print(t)