file = open("day14_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

mem = {}
mask = [None]*36
for line in lines:
    command, num = line.split(' = ')
    if command == 'mask':
        for i in range(len(mask)):
            mask[i] = None if num[i] == 'X' else num[i]
    else:
        index = command.split('[')[1].rstrip(']')
        b_num = '{:036b}'.format(int(num))
        b_num_with_mask = ''
        for i in range(len(mask)):
            if mask[i] is not None:
                b_num_with_mask += mask[i] 
            else:
                b_num_with_mask += b_num[i]
        num_with_mask = int(b_num_with_mask, 2)
        mem[index] = num_with_mask
        
print(sum(mem.values()))