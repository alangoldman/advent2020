file = open("day19_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

rules = {}
def test(s, rule=None):
    #print(s, rule)
    if rule is None:
        rule = rules['0']
    if s == '':
        return (False, '')

    if rule.startswith('"'):
        return (s[0] == rule[1], s[1:])

    if '|' in rule:
        subrule1, subrule2 = rule.split(' | ')
        subrule1_test = test(s, subrule1)
        subrule2_test = test(s, subrule2)
        if subrule1_test[0]:
            return (True, subrule1_test[1])
        elif subrule2_test[0]:
            return (True, subrule2_test[1])
        else:
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
            continue
        key, value = line.split(': ')
        rules[key] = value
    else:
        result = test(line)
        if result[0] and result[1] == '':
            print(line)
            matches += 1
            
print(matches)