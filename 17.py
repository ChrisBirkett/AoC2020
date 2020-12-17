import copy
import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]
slice_size = len(lines)
boot_iterations = 6

original_model = [[[[False for z in range(boot_iterations * 2 + 1)]
                    for y in range(boot_iterations * 2 + slice_size)]
                   for x in range(boot_iterations * 2 + slice_size)]
                  for w in range(boot_iterations * 2 + 1)]
# size 13,20x20x13, start at 6,6,6,6 i.e. place 1x8x8x1 in centre
# FWIW :) it turns out this would have been much easier with tuple coordinates
for x in range(slice_size):
    for y in range(slice_size):
        original_model[boot_iterations][x+boot_iterations][y+boot_iterations][boot_iterations] = lines[x][y] == '#'


def get_number_of_active_neighbours(model, w, x, y, z):
    steps = [(wd, xd, yd, zd)
             for wd in range(-1, 2)
             for xd in range(-1, 2)
             for yd in range(-1, 2)
             for zd in range(-1, 2) if not (wd == xd == yd == zd == 0)]
    return sum([model[w + wd][x + xd][y + yd][z + zd]
                for wd, xd, yd, zd in steps
                if 0 <= w + wd < len(model)
                and 0 <= x + xd < len(model[0])
                and 0 <= y + yd < len(model[0][0])
                and 0 <= z + zd < len(model[0][0][0])])


def get_new_state(model, w, x, y, z):
    active_neighbours = get_number_of_active_neighbours(model, w, x, y, z)
    if model[w][x][y][z]:
        return 2 <= active_neighbours <= 3
    return active_neighbours == 3


current_model = original_model
for i in range(boot_iterations):
    new_model = copy.deepcopy(current_model)
    for w in range(len(current_model)):
        for x in range(len(current_model[0])):
            for y in range(len(current_model[0][0])):
                for z in range(len(current_model[0][0][0])):
                    new_model[w][x][y][z] = get_new_state(current_model, w, x, y, z)
    current_model = new_model

# Remove w dimension for part 1
print(sum([current_model[w][x][y][z]
           for w in range(len(current_model))
           for x in range(len(current_model[0]))
           for y in range(len(current_model[0][0]))
           for z in range(len(current_model[0][0][0]))]))
