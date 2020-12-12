import fileinput
import itertools

numbers = [int(line) for line in fileinput.input()]


def part1():
    for x, y in itertools.product(numbers, numbers):
        if x + y == 2020:
            return x * y


def part2():
    for x, y, z in itertools.product(numbers, numbers, numbers):
        if x + y + z == 2020:
            return x * y * z



print(part1())
print(part2())
