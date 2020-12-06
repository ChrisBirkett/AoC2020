import fileinput

lines = [line for line in fileinput.input()]
group_lines = [line.replace('\n', ' ').split(' ') for line in ''.join(lines).split('\n\n')]


def part1():
    counts = 0
    for group in group_lines:
        answers = ''.join(group)
        distinct_answers = set(answers)
        counts += len(distinct_answers)
    return counts


def part2():
    counts = 0
    for group in group_lines:
        shared_answers = set.intersection(*list(map(set, group)))
        counts += len(shared_answers)
    return counts


print(part1())
print(part2())