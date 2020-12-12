import fileinput

numbers = [int(line.replace('\n', '')) for line in fileinput.input()]


def is_valid_idx(idx):
    for x in range(idx-25, idx):
        for y in range(x+1, idx):
            if numbers[x] + numbers[y] == numbers[idx]:
                return True
    return False


def part1():
    for idx in range(25, len(numbers)):
        if not is_valid_idx(idx):
            return numbers[idx]


def part2(part1_result):
    for x in range(25, len(numbers)):
        for y in range(x+1, len(numbers)):
            section = list(map(lambda z: numbers[z], range(x, y+1)))
            section_sum = sum(section)
            if section_sum > part1_result:
                break
            if section_sum == part1_result:
                return min(section) + max(section)


part1 = part1()
print(part1)
print(part2(part1))
