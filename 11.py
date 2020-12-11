import copy
import fileinput

original_layout = [line.replace('\n', '') for line in fileinput.input()]
rows = len(original_layout)
cols = len(original_layout[0])
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def num_occupied_adjacent_seats(layout, row, col):
    adjacent_occupied_counter = 0
    for direction in directions:
        search_row = row + direction[0]
        search_col = col + direction[1]
        if not 0 <= search_row < rows or not 0 <= search_col < cols:
            continue
        adjacent_occupied_counter += layout[search_row][search_col] == '#'
    return adjacent_occupied_counter


def num_occupied_visible_seats(layout, row, col):
    occupied_visible = 0
    for direction in directions:
        for distance in range(1, rows):
            travel = tuple(i * distance for i in direction)
            search_row = row + travel[0]
            search_col = col + travel[1]
            if not 0 <= search_row < rows or not 0 <= search_col < cols:
                continue
            if layout[search_row][search_col] == '#':
                occupied_visible += 1
            if layout[search_row][search_col] != '.':
                break
    return occupied_visible


def iterate(layout, f, tolerance):
    new_layout = copy.deepcopy(layout)
    seats_moved = False
    for col in range(cols):
        for row in range(rows):
            visible_neighbours = f(layout, row, col)
            if layout[row][col] == 'L' and not visible_neighbours:
                new_layout[row] = new_layout[row][:col] + '#' + new_layout[row][col+1:]
                seats_moved = True
            if layout[row][col] == '#' and visible_neighbours >= tolerance:
                new_layout[row] = new_layout[row][:col] + 'L' + new_layout[row][col+1:]
                seats_moved = True
    return new_layout, seats_moved


def run(count_fn, threshold):
    layout = copy.deepcopy(original_layout)
    while True:
        layout, seats_moved = iterate(layout, count_fn, threshold)
        if not seats_moved:
            break
    return sum([layout[y][x] == '#' for y in range(rows) for x in range(cols)])


def part1():
    return run(num_occupied_adjacent_seats, 4)


def part2():
    return run(num_occupied_visible_seats, 5)


print(part1())
print(part2())
