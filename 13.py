import fileinput
from modint import chinese_remainder

lines = [line.replace('\n', '') for line in fileinput.input()]
buses = [int(x) if x != 'x' else 'x' for x in lines[1].split(',')]


def part1():
    earliest_departure = int(lines[0])
    waits = []
    for bus in buses:
        if bus != 'x':
            num_missed = int(earliest_departure / bus)
            waits.append((bus, (bus * (num_missed + 1)) % earliest_departure))
    min_wait = min(waits, key=lambda t: t[1])
    return min_wait[0] * min_wait[1]


def part2():
    crt_n = []
    crt_a = []
    for idx, bus in enumerate(buses):
        if bus != 'x':
            crt_n.append(bus)
            crt_a.append(bus - idx)
    return chinese_remainder(crt_n, crt_a)


print(part1())
print(part2())
