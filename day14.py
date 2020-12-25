file = open("day14_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

def enumerate_indexes(index):
    result = []
    try:
        i = index.index('X')
        new_index = index[:i]
        sub_index = index[i+1:]
        sub_result = enumerate_indexes(sub_index)
        result += [new_index + '0' + e for e in sub_result]
        result += [new_index + '1' + e for e in sub_result]
        return result
    except ValueError:
        return [index]

mem = {}
mask = [None]*36
for line in lines:
    command, num = line.split(' = ')
    if command == 'mask':
        for i in range(len(mask)):
            mask[i] = None if num[i] == 'X' else num[i]
    else:
        index = command.split('[')[1].rstrip(']')
        b_index = '{:036b}'.format(int(index))
        b_index_with_mask = ''
        for i in range(len(mask)):
            if mask[i] is None:
                b_index_with_mask += 'X'
            elif mask[i] == '0':
                b_index_with_mask += b_index[i] 
            elif mask[i] == '1':
                b_index_with_mask += '1'
                
        for i in enumerate_indexes(b_index_with_mask):
            mem[i] = int(num)
        
print(sum(mem.values()))