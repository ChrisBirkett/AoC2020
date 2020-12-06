import fileinput

lines = [line for line in fileinput.input()]
group_lines = [line.replace('\n', ' ').split(' ') for line in ''.join(lines).split('\n\n')]

part1 = part2 = 0

for group in group_lines:
    all_answers = ''.join(group)
    distinct_answers = set(all_answers)
    shared_answers = set.intersection(*list(map(set, group)))
    part1 += len(distinct_answers)
    part2 += len(shared_answers)

print(part1)
print(part2)
