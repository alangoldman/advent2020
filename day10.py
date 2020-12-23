file = open("day10_input.txt", "r")
adapters = [int(l.rstrip()) for l in file.readlines()]
file.close()

device = max(adapters)+3

adapters.sort()
last_adapter = 0
diffs = {0:0, 1:0, 2:0, 3:0}
dp = [0]*(device+1)
dp[0] = 1 # part 2

while len(adapters) > 0:
    adapter = adapters.pop(0)
    for i in range(1,4): # 1, 2, and 3 lower
        if adapter-i >= 0: # but in bounds!
            dp[adapter] += dp[adapter-i]
    diff = adapter - last_adapter
    diffs[diff] += 1
    last_adapter = adapter
    
diffs[device-last_adapter] += 1
print(diffs[1]*diffs[3])

print(dp[adapter])