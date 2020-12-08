import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]


def run(instructions, return_acc_on_cycle):
    acc = 0
    idx = 0
    idx_used = set()
    while True:
        if idx >= len(instructions):
            return acc
        if idx in idx_used:
            return acc if return_acc_on_cycle else None
        idx_used.add(idx)
        instruction, value = instructions[idx].split(' ')
        if instruction == 'nop':
            idx += 1
        elif instruction == 'acc':
            acc += int(value)
            idx += 1
        elif instruction == 'jmp':
            idx += int(value)


def part1():
    return run(lines, True)


def part2():
    for i in range(len(lines)):
        instructions = [*lines]
        instruction, value = instructions[i].split(' ')
        if instruction == 'acc':
            continue
        if instruction == 'jmp' and int(value) == 0:
            continue
        if instruction == 'nop':
            instructions[i] = 'jmp ' + value
        elif instruction == 'jmp':
            instructions[i] = 'nop ' + value
        result = run(instructions, False)
        if result is not None:
            return result


print(part1())
print(part2())
