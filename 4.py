import fileinput
import re

lines = [line for line in fileinput.input()]
passport_lines = [line.replace('\n', ' ').split(' ') for line in ''.join(lines).split('\n\n')]


def make_passport(line):
    passport = {}
    for field in line:
        field_name, field_value = field.split(':')
        passport[field_name] = field_value
    return passport


passports = [make_passport(line) for line in passport_lines]


four_digits = re.compile(r"^\d{4}$")
hair_colour = re.compile(r"^#[0-9a-f]{6}")
eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
pid = re.compile(r"^\d{9}$")
rules = {
    "byr": lambda x: re.search(four_digits, x) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: re.search(four_digits, x) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: re.search(four_digits, x) and 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.search(hair_colour, x),
    "ecl": lambda x: x in eye_colours,
    "pid": lambda x: re.search(pid, x)
}
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def is_valid_passport_1(passport):
    return set(passport.keys()).issuperset(required_fields)


def is_valid_passport_2(passport):
    if not is_valid_passport_1(passport):
        return False
    for field_name in required_fields:
        field_value = passport[field_name]
        field_rule = rules[field_name]
        if not field_rule(field_value):
            return False
    return True


def run(passport_checker):
    return len([1 for passport in passports if passport_checker(passport)])


print(run(is_valid_passport_1))
print(run(is_valid_passport_2))
