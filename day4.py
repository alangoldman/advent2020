import re

file = open("day4_input.txt", "r")
lines = file.readlines()
file.close()

passports = []
passport = ''
for l in lines:
	l = l.rstrip()
	if l == '' and passport:
		passports.append(passport)
		passport = ''
	else:
		passport += l+' '
		
if passport != '':
	passports.append(passport)
	
	
required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) #'cid'
valid = 0
for passport in passports:
	fields = set([s.split(':')[0] for s in passport.split(' ') if s.strip() != ''])
	if len(required_fields - fields) == 0:
		valid += 1
		
print(valid)

#part 2
hex_rex = re.compile('^#[0-9a-f]{6}$')
id_rex = re.compile('^[0-9]{9}$')
valid_eye = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
valid = 0
for passport in passports:
	fields = {(s.split(':')[0]):(s.split(':')[1]) for s in passport.split(' ') if s.strip() != ''}
	if len(required_fields - fields.keys()) != 0:
		continue
		
	byr = int(fields['byr'])
	iyr = int(fields['iyr'])
	eyr = int(fields['eyr'])
	hgt = fields['hgt']
	hcl = fields['hcl']
	ecl = fields['ecl']
	pid = fields['pid']
		
	if not 1920 <= byr <= 2002:
		continue
		
	if not 2010 <= iyr <= 2020:
		continue
		
	if not 2020 <= eyr <= 2030:
		continue
		
	metric = hgt[-2:] == 'cm'
	imperial = hgt[-2:] == 'in'
	if not metric and not imperial:
		continue

	height = int(hgt[0:-2])
	if metric and not 150 <= height <= 193:
		continue
	if imperial and not 59 <= height <= 76:
		continue
		
	if not hex_rex.match(hcl):
		continue
		
	if ecl not in valid_eye:
		continue
		
	if not id_rex.match(pid):
		continue
	valid += 1

print(valid)