import fileinput
import math
import re

lines = [line.replace('\n', '') for line in fileinput.input()]
my_ticket = list(map(int, lines[22].split(',')))
nearby_tickets = [list(map(int, line.split(','))) for line in lines[25:]]
rule_regex = re.compile(r"([\w ]*): (\d*)-(\d*) or (\d*)-(\d*)")
rules = [rule_regex.match(line).groups() for line in lines[:20]]
rules = [(rule[0], int(rule[1]), int(rule[2]), int(rule[3]), int(rule[4])) for rule in rules]


def is_value_invalid(num):
    for rule in rules:
        if rule[1] <= num <= rule[2] or rule[3] <= num <= rule[4]:
            return False
    return True


def is_ticket_invalid(ticket):
    for num in ticket:
        if is_value_invalid(num):
            return True
    return False


def part1():
    invalid_numbers = [num for ticket in nearby_tickets for num in ticket if is_value_invalid(num)]
    return sum(invalid_numbers)


def part2():
    valid_tickets = [ticket for ticket in nearby_tickets if not is_ticket_invalid(ticket)]
    valid_tickets.sort(key=lambda t: t[0])
    rules.sort(key=lambda t: t[1])
    compatible_rules = [list(map(lambda x: x[0], rules)) for i in range(20)]
    confirmed_rules = ['' for i in range(20)]

    for ticket in valid_tickets:
        for idx, num in enumerate(ticket):
            for rule in rules:
                if rule[0] not in compatible_rules[idx]:
                    continue
                if not (rule[1] <= num <= rule[2] or rule[3] <= num <= rule[4]):
                    compatible_rules[idx].remove(rule[0])

    while sum(map(len, compatible_rules)):  # then some rules have multiple options
        for idx, rule_options in enumerate(compatible_rules):
            if len(rule_options) == 1:
                confirmed_rules[idx] = rule_options[0]
                for idx_r, r in enumerate(compatible_rules):
                    if rule_options[0] in r:
                        compatible_rules[idx_r] = [rule_name for rule_name in compatible_rules[idx_r] if rule_name != rule_options[0]]
                break

    my_ticket_departure_values = [x for idx, x in enumerate(my_ticket) if 'departure' in confirmed_rules[idx]]
    return math.prod(my_ticket_departure_values)


print(part1())
print(part2())
