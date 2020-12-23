file = open("day12_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

heading = 0
    # east  south   west    north
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
x, y = (0, 0)
w_x, w_y = (10, 1)

for line in lines:
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
        sign = -1 if command == 'L' else 1
        heading += sign*int(dist/90)
    heading %= 4
    if command == 'F':
        x += w_x*dist
        y += y_x*dist
        
print(x,y,abs(x)+abs(y))