import fileinput
import math

lines = [line.replace('\n', '') for line in fileinput.input()]
tiles_str = '\n'.join(lines).split('\n\n')
tiles = {tile_str.split('\n')[0][5:9]: tile_str.split('\n')[1:] for tile_str in tiles_str}
tile_size = 10


def get_borders(tile):
    top, bottom = tile[0], tile[tile_size - 1]
    left = right = ''
    for i in range(tile_size):
        left += tile[i][0]
        right += tile[i][tile_size - 1]
    return top, bottom, left, right


def get_shared_borders(border_patterns, tile_id):
    top, bottom, left, right = border_patterns[tile_id]
    shared_borders = set()
    for s_tile_id, (s_top, s_bottom, s_left, s_right) in border_patterns.items():
        if s_tile_id == tile_id:
            continue
        shared_border = {top, bottom, left, right, top[::-1], bottom[::-1], left[::-1], right[::-1]}\
            .intersection({s_top, s_bottom, s_left, s_right})
        shared_borders = shared_borders.union(shared_border)
    return shared_borders


def part1():
    border_patterns = {tile_id: get_borders(tile) for tile_id, tile in tiles.items()}
    return math.prod(int(tile_id)
                     for tile_id in tiles.keys()
                     if len(get_shared_borders(border_patterns, tile_id)) == 2)


def part2():
    return


print(part1())
print(part2())
