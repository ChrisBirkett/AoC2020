import fileinput

data = [line.replace('\n', '') for line in fileinput.input()]
map_length = len(data)
map_width = len(data[0])


def is_tree(y, x):
    return data[y][x] == '#'


def count_trees(gradient_y, gradient_x):
    pos_x = tree_counter = 0
    for pos_y in range(0, map_length, gradient_y):
        if is_tree(pos_y, pos_x):
            tree_counter += 1
        pos_x = (pos_x + gradient_x) % map_width
    return tree_counter


def part1():
    return count_trees(1, 3)


def part2():
    weird_accumulator = 1
    for y, x in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        weird_accumulator *= count_trees(y, x)
    return weird_accumulator


print(part1())
print(part2())
