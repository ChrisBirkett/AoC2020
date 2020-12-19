import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]
separator = lines.index('')
rules = {int(k): v.split(" | ") for k, v in map(lambda r: r.split(': '), lines[:separator])}
messages = lines[separator+1:]


def matches_option(message, option):
    if option == '"a"' or option == '"b"':
        return message.startswith(option.replace('"', '')), 1
    option_rule_sequence = list(map(lambda x: int(x), option.split(' ')))
    chars_matched = 0
    for option_rule in option_rule_sequence:
        matches, chars_matched_by_rule = matches_rule(message[chars_matched:], option_rule, False)
        if not matches:
            return False, 0
        chars_matched += chars_matched_by_rule
    return True, chars_matched


def matches_rule(message, number, complete):
    rule = rules[number]
    chars_matched = 0
    for option in rule:
        matches, chars_matched_by_option = matches_option(message, option)
        if matches:
            chars_matched += chars_matched_by_option
            return not complete or chars_matched == len(message), chars_matched_by_option
    return False, 0


def part1():
    return sum([matches_rule(message, 0, True)[0] for message in messages])


def part2():
    rules[8] = ['42', '42 8']
    rules[11] = ['42 31', '42 11 31']
    # > 188
    # generic linear approach does not work
    # need a DAG / non-generic
    # SO TIRED
    return sum([matches_rule(message, 0, True)[0] for message in messages])


# print(part1())
print(part2())
