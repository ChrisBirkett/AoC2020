import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]


def get_num(loc, flag_upper):
    binary_str = ''.join(['1' if c == flag_upper else '0' for c in loc])
    return int(binary_str, 2)


def get_seats():
    ids = {}
    for line in lines:
        row = line[:-3]
        col = line[-3:]
        row_num = get_num(row, 'B')
        col_num = get_num(col, 'R')
        seat_id = int(row_num * 8 + col_num)
        ids[seat_id] = True
    return ids


seats = get_seats()
seat_ids = seats.keys()
min_seat_id = min(seat_ids)
max_seat_id = max(seat_ids)


def part1():
    return max_seat_id


def part2():
    for i in range(min_seat_id, max_seat_id):
        if i in seats or i+1 not in seats or i+2 not in seats:
            continue
        return i


print(part1())
print(part2())
