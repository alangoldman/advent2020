import string
file = open("day11_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

rows = len(lines)
cols = len(lines[0])

conway = [['.' for i in range(cols+2)] for j in range(rows+2)]
for i in range(0, rows):
    for j in range(0, cols):
        conway[i+1][j+1] = lines[i][j]
        
changes = ['Nop']
while len(changes) > 0:
    while len(changes) > 0:
        (i, j, c) = changes.pop()
        if c == 'p':
            continue
        conway[i][j] = c

    for i in range(1, rows+1):
        for j in range(1, cols+1):
            neighbors = 0
            
            """
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if conway[i+dy][j+dx] == '#':
                        neighbors += 1
            """
            
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    i_n = i+dy
                    j_n = j+dx
                    while 0 <= i_n < rows+2 and \
                        0 <= j_n < cols+2:
                        c_n = conway[i_n][j_n]
                        if c_n == 'L' or c_n == '#':
                            neighbors += 1 if c_n == '#' else 0
                            break
                        i_n = i_n+dy
                        j_n = j_n+dx
                        
            if conway[i][j] == 'L' and neighbors == 0:
                changes.append((i,j,'#'))
            elif conway[i][j] == '#' and neighbors >= 5:
                changes.append((i,j,'L'))

occupied = 0     
for i in range(1, rows+1):
    for j in range(1, cols+1):
        if conway[i][j] == '#':
            occupied += 1
print(occupied)

