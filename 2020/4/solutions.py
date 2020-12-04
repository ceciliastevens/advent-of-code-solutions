import re
VALID_PASSPORT_FIELDS = [
	("byr", lambda x: 1920 <= int(x) <= 2002),
	("iyr", lambda x: 2010 <= int(x) <= 2020),
	("eyr", lambda x: 2020 <= int(x) <= 2030),
	("hgt", lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)),
	("hcl", lambda x: re.match("^#[0-9a-f]{6}$", x)),
	("ecl", lambda x: re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", x)),
	("pid", lambda x: re.match("^[0-9]{9}$", x)),
#	"cid", # allow this to be missing in puzzle 1
]

def is_passport_valid(passport, valid_passport_fields, test=False):
	for field, function in valid_passport_fields:
		if test and field in passport.keys():
			if not function(passport[field]):
				return False
		if field not in passport.keys():
			return False
	return True

# really sloppy input processing
def get_input(filename):
	with open(filename, "r") as in_file:
		list_of_dicts = []
		dict_index = 0
		for line in in_file.readlines():
			if len(list_of_dicts) <= dict_index:
				list_of_dicts.append({})
			if line.strip() == "":
				dict_index += 1
				continue
			for pair in line.strip().split(" "):
				list_of_dicts[dict_index].update({pair.split(":")[0]: pair.split(":")[1]})
	return list_of_dicts

puzzle_input = get_input("input.txt")

#puzzle 1 solution
valid_passports = 0
for passport in puzzle_input:
	if is_passport_valid(passport, VALID_PASSPORT_FIELDS):
		valid_passports += 1

print("At first there are {} valid passports".format(valid_passports))

#puzzle 2 solution
valid_passports = 0
for passport in puzzle_input:
	if is_passport_valid(passport, VALID_PASSPORT_FIELDS, test=True):
		valid_passports += 1

print("Using stricter validation, there are {} valid passports".format(valid_passports))