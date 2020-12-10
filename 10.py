import fileinput
import itertools

numbers = [int(line.replace('\n', '')) for line in fileinput.input()]
numbers.sort()


def part1():
    joltage = 0
    jumps1 = jumps3 = 0
    for number in numbers:
        if number - joltage == 1:
            jumps1 += 1
        elif number - joltage == 3:
            jumps3 += 1
        joltage = number

    jumps3 += 1
    return jumps1 * jumps3


def part2():
    # this is far, far too complicated... totally unnecessary!
    subgroups = []
    current_subgroup = []
    for idx, number in enumerate(numbers):
        if idx > 0 and number - numbers[idx-1] == 3:
            subgroups.append(current_subgroup)
            current_subgroup = [number]
        elif idx == len(numbers)-1:
            current_subgroup.append(number)
            subgroups.append(current_subgroup)
        else:
            current_subgroup.append(number)

    def get_prev(num):
        idx = numbers.index(num)
        return numbers[idx-1] if idx > 0 else 0

    def get_next(num):
        idx = numbers.index(num)
        if idx < len(numbers)-1:
            return numbers[idx+1]

    def is_valid_arrangement(arrangement, prev, next):
        # must connect to prev
        if arrangement[0] - prev > 3:
            return False
        # must contain final adapter if end
        if next is None and max(numbers) not in arrangement:
            return False
        # must connect to next
        if next is not None and next - arrangement[len(arrangement) - 1] > 3:
            return False
        # must not contain jumps > 3
        for idx, number in enumerate(arrangement):
            if idx > 0 and number - arrangement[idx - 1] > 3:
                return False
        return True

    num_arrangements = 1
    for subgroup in subgroups:
        valid_arrangement = 0
        for i in range(1, len(subgroups)+1):
            arrangement = list(itertools.combinations(subgroup, i))
            # make sure the arrangement connects to adjacent arrangement
            prev = get_prev(min(subgroup))
            next = get_next(max(subgroup))
            valid_arrangement += sum([is_valid_arrangement(c, prev, next) for c in arrangement])
        num_arrangements *= valid_arrangement

    return num_arrangements


print(part1())
print(part2())
