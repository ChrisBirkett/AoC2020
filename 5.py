import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]


def get_num(loc, flag_upper):
    binary_str = ''.join([str(int(c == flag_upper)) for c in loc])
    return int(binary_str, 2)


def get_seats():
    ids = set()
    for line in lines:
        row = line[:-3]
        col = line[-3:]
        row_num = get_num(row, 'B')
        col_num = get_num(col, 'R')
        seat_id = int(row_num * 8 + col_num)
        ids.add(seat_id)
    return ids


seat_ids = get_seats()
min_seat_id = min(seat_ids)
max_seat_id = max(seat_ids)


def part1():
    return max_seat_id


def part2():
    for i in range(min_seat_id, max_seat_id):
        if i+1 in seat_ids or i not in seat_ids or i+2 not in seat_ids:
            continue
        return i+1


print(part1())
print(part2())
