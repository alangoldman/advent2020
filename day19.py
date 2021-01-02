file = open("day19_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

rules = {}
def test(s, rule=None):
    if rule is None:
        rule = rules['0']
    #print(s, rule)
    
    if s == '':
        return (False, [])

    if rule.startswith('"'):
        return (s[0] == rule[1], [s[1:]])

    if '|' in rule:
        subrules = rule.split(' | ')
        matches = []
        for subrule in subrules:
            subrule_test = test(s, subrule)
            if subrule_test[0]:
                matches += subrule_test[1]
        return (len(matches)>0, matches)
    else:
        subrules = rule.split(' ')
        matches = [s]
        for subrule in subrules:
            next_matches = []
            for match in matches:
                subrule_test = test(match, rules[subrule])
                if subrule_test[0]:
                    next_matches += subrule_test[1]
            if len(next_matches) == 0:
                return (False, [])
            matches = next_matches
        return (True, matches)
    
    
rule_mode = True
matches = 0
for line in lines:
    if rule_mode:
        if line == '':
            rule_mode = False
            rules['8'] = '42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42'
            rules['11'] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31'
            continue
        key, value = line.split(': ')
        rules[key] = value
    else:
        #line = 'aaaaabbaabaaaaababaa'
        #line = 'babbbbaabbbbbabbbbbbaabaaabaaa'
        result = test(line)
        if result[0] and '' in result[1]:
            print(line)
            matches += 1
        #break
            
print(matches)