file = open("day12_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

x, y = (0, 0)
w_x, w_y = (10, 1)

for line in lines:
    print(x, y, w_x, w_y)
    command = line[0]
    dist = int(line[1:])
    if command == 'N':
        w_y += dist
    if command == 'S':
        w_y -= dist
    if command == 'E':
        w_x += dist
    if command == 'W':
        w_x -= dist
    if command == 'L' or command == 'R':
        for i in range(int(dist/90)):
            sign_x = -1 if command == 'R' else 1
            sign_y = -1 if command == 'L' else 1
            w_x, w_y = (w_y*sign_y, w_x*sign_x)
    if command == 'F':
        x += w_x*dist
        y += w_y*dist
        
print(x,y,abs(x)+abs(y))