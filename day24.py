import numpy as np
file = open("day24_input.example.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

size = 150
floor = np.zeros((size, size), int)
reference = (int(size/2), int(size/2))

dirs_odd = {
    'e': (0, 1),
    'se': (1, 1),
    'sw': (1, 0),
    'w': (0, -1),
    'nw': (-1, 0),
    'ne': (-1, 1),
}
dirs_even = {
    'e': (0, 1),
    'se': (1, 0),
    'sw': (1, -1),
    'w': (0, -1),
    'nw': (-1, -1),
    'ne': (-1, 0),
}

for move in lines:
    pointer = reference
    i = 0
    while i < len(move):
        dirs = dirs_even if pointer[0] % 2 == 0 else dirs_odd
        d = move[i]
        if d not in dirs:
            i += 1
            d += move[i]

        pointer = (pointer[0] + dirs[d][0], pointer[1] + dirs[d][1])
        i += 1

    floor[pointer] = 1 if floor[pointer] == 0 else 0 # 0=white, 1=black

for day in range(1, 101):
    new_floor = floor.copy()
    for row in range(2, size-2):
        for col in range(2, size-2):
            dirs = dirs_even if row % 2 == 0 else dirs_odd
            black = 0
            for d in dirs.keys():
                black += floor[row + dirs[d][0], col + dirs[d][1]]
            if floor[row, col] == 1 and black == 0 or black > 2:
                new_floor[row, col] = 0
            elif floor[row, col] == 0 and black == 2:
                new_floor[row, col] = 1
    floor = new_floor

print(day, np.count_nonzero(floor))
