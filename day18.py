file = open("day18_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

def eval(s):
    last_num = None
    last_op = None
    i = -1
    while i < len(s)-1:
        i += 1
        n = 0
        if s[i] == ' ':
            continue
        elif s[i] == '(':
            start = i+1
            indent = 1
            while indent > 0:
                i += 1
                if s[i] == '(':
                    indent += 1
                elif s[i] == ')':
                    indent -= 1
            n = eval(s[start:i])
        elif s[i].isdigit():
            while i < len(s) and s[i].isdigit():
                n = n*10 + int(s[i])
                i += 1
        elif s[i] in ['+', '*']:
            last_op = s[i]
            if s[i] == '*':
                n = eval(s[i+1:])
                i = len(s)
            else:
                continue
            
        if last_num == None:
            last_num = n
        elif last_op == '+':
            last_num += n
        elif last_op == '*':
            last_num *= n
                
    return last_num
    
print(eval('1 + 2 * 3 + 4 * 5 + 6'))
print(eval('1 + (2 * 3) + (4 * (5 + 6))'))
print(eval('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))


total = 0
for equation in lines:
    total += eval(equation)
    
print(total)