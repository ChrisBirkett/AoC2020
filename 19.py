import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]
separator = lines.index('')
rules = {int(k): v.split(" | ") for k, v in map(lambda r: r.split(': '), lines[:separator])}
messages = lines[separator+1:]


def get_remainders(message, rule):
    for option in rule:
        if option.startswith('"'):
            if message.startswith(option[1]):
                yield message[1:]
            continue
        rem_sfx = [message]
        for option_rule in option.split(' '):
            rem_sfx = [r for suffix in rem_sfx for r in get_remainders(suffix, rules[int(option_rule)])]
        for suffix in rem_sfx:
            yield suffix


def part1():
    return sum(['' in get_remainders(message, rules[0]) for message in messages])


def part2():
    rules[8] = ['42', '42 8']
    rules[11] = ['42 31', '42 11 31']
    return sum(['' in get_remainders(message, rules[0]) for message in messages])


print(part1())
print(part2())
