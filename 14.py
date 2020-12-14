import fileinput

lines = [line.replace('\n', '').split(' = ') for line in fileinput.input()]


def apply_p1_mask(value, mask):
    value = value & int('0b' + mask.replace('X', '1'), 2)
    value = value | int('0b' + mask.replace('X', '0'), 2)
    return value


def apply_p2_mask(value, mask):
    bin_value = bin(value).lstrip('0b')
    bin_value = '0' * (len(mask) - len(bin_value)) + bin_value
    acc = ''
    for idx, c in enumerate(mask):
        if mask[idx] == '0':
            acc += bin_value[idx]
        else:
            acc += mask[idx]
    return acc


def get_p2_addresses(mask):
    x_loc = mask.find('X')
    if x_loc == -1:
        return [mask]
    mask0 = mask[:x_loc] + '0' + mask[x_loc+1:]
    mask1 = mask[:x_loc] + '1' + mask[x_loc+1:]
    return get_p2_addresses(mask0) + get_p2_addresses(mask1)


def part1():
    memory = {}
    mask = None
    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
        else:
            key = line[0][4:-1]
            memory[key] = apply_p1_mask(int(line[1]), mask)
    return sum(memory.values())


def part2():
    memory = {}
    mask = None
    for line in lines:
        if line[0] == 'mask':
            mask = line[1]
        else:
            key = line[0][4:-1]
            key_mask = apply_p2_mask(int(key), mask)
            addresses = get_p2_addresses(key_mask)
            for m in addresses:
                addr = apply_p1_mask(int(key), m)
                memory[addr] = int(line[1])
    return sum(memory.values())


print(part1())
print(part2())
