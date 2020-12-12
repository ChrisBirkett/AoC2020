import fileinput
import re

exp = re.compile(r"(\d*)-(\d*) (\w): (\w*)")
lines = [exp.match(line).groups() for line in fileinput.input()]


def part1():
    match_counter = 0
    for policy_lower, policy_upper, char, pw in lines:
        matches = pw.count(char)
        if int(policy_lower) <= matches <= int(policy_upper):
            match_counter += 1
    return match_counter


def part2():
    match_counter = 0
    for policy_idx1, policy_idx2, char, pw in lines:
        char1_match = pw[int(policy_idx1) - 1] == char
        char2_match = pw[int(policy_idx2) - 1] == char
        if char1_match ^ char2_match:
            match_counter += 1
    return match_counter


print(part1())
print(part2())
