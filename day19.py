file = open("day19_input.example2.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

rules = {}
def test(s, rule=None):
    if rule is None:
        rule = rules['0']
    print(s, rule)
    
    if s == '':
        return (False, None)

    if rule.startswith('"'):
        return (s[0] == rule[1], s[1:])

    if '|' in rule:
        subrules = rule.split(' | ')
        for subrule in subrules:
            subrule_test = test(s, subrule)
            if subrule_test[0]:
                return (True, subrule_test[1])
        return (False, None)
    else:
        subrules = rule.split(' ')
        for subrule in subrules:
            subrule_test = test(s, rules[subrule])
            if subrule_test[0]:
                s = subrule_test[1]
            else:
                return (False, None)
        return (True, s)
    
    
rule_mode = True
matches = 0
for line in lines:
    if rule_mode:
        if line == '':
            rule_mode = False
            rules['8'] = '42 | 42 42'
            rules['11'] = '42 31 | 42 42 31 31'
            continue
        key, value = line.split(': ')
        rules[key] = value
    else:
        line = 'aaaaabbaabaaaaababaa'
        #line = 'aaaabbaaaabbaaa'
        result = test(line)
        if result[0] and result[1] == '':
            print(line)
            matches += 1
        break
            
print(matches)