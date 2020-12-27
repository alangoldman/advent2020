from numpy import zeros
file = open("day17_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

z = 0
scale = 5
max_cycles = 6
max_x = len(lines[0])*scale
max_y = len(lines)*scale
max_z = max_cycles*scale

grid = zeros([max_x, max_y, max_z])

for x in range(len(lines[0])):
    for y in range(len(lines)):
        if lines[x][y] == '#':
            print(x,y,z)
            grid[x][y][z] = 1
            

for iteration in range(max_cycles):
    new_active = 0
    new_grid = zeros([max_x, max_y, max_z])
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                neighbors = 0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        for dz in range(-1,2):
                            if dx==0 and dy==0 and dz==0:
                                continue
                            if grid[(x+dx)%max_x, (y+dy)%max_y, (z+dz)%max_z]==1:
                                neighbors += 1
                if grid[x,y,z]==1 and 2<= neighbors<= 3:
                    new_grid[x,y,z] = 1
                    new_active += 1
                elif grid[x,y,z]==0 and neighbors==3:
                    new_grid[x,y,z] = 1
                    new_active += 1
    grid = new_grid