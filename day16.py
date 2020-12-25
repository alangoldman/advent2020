file = open("day16_input.txt", "r")
lines = [l.rstrip() for l in file.readlines()]
file.close()

class rule:
    def __init__(self, line):
        self.name, ranges = line.split(': ')
        self.validnums = set()

        range1, range2 = ranges.split(' or ')
        r1low, r1high = [int(i) for i in range1.split('-')]
        r2low, r2high = [int(i) for i in range2.split('-')]
        self.validnums.update(range(r1low, r1high+1))
        self.validnums.update(range(r2low, r2high+1))
    
    def isValid(self, n):
        return n in self.validnums
    
    def getValidIndexes(self, ticket):
        result = set()
        for i in range(len(ticket)):
            if self.isValid(ticket[i]):
                result.add(i)
        return result
    
rules = []
rule_mode = True
ticket_mode = False
nearby_mode = False

your_ticket = []
nearby_tickets = []

for line in lines:
    if line == '':
        continue
    elif line == 'your ticket:':
        rule_mode = False
        ticket_mode = True
        nearby_mode = False
    elif line == 'nearby tickets:':
        rule_mode = False
        ticket_mode = False
        nearby_mode = True
    elif rule_mode:
        rules.append(rule(line))
    elif ticket_mode:
        your_ticket = [int(i) for i in line.split(',')]
    elif nearby_mode:
        nearby_tickets.append([int(i) for i in line.split(',')])
        
invalid_sum = 0
valid_tickets = []
for ticket in nearby_tickets:
    ticket_valid = True
    for num in ticket:
        any_valid = False
        for rule in rules:
            if rule.isValid(num):
                any_valid = True
                
        if not any_valid:
            invalid_sum += num
            ticket_valid = False
    if ticket_valid:
        valid_tickets.append(ticket)
                
ordered_rules = {}
unordered_rules = set(rules)
while len(ordered_rules.keys()) < len(rules):
    new_unordered_rules = set()
    for rule in unordered_rules:
        valid_indexes = set(range(len(rules))) - set(ordered_rules.keys())
        for ticket in valid_tickets:
            valid_indexes = valid_indexes.intersection(rule.getValidIndexes(ticket))

        if len(valid_indexes) == 1:
            ordered_rules[valid_indexes.pop()] = rule
        new_unordered_rules.add(rule)
    unordered_rules = new_unordered_rules

answer = 1
for i in range(len(rules)):
    rule = ordered_rules[i]
    if rule.name.startswith('departure'):
        answer *= your_ticket[i]
print(answer)