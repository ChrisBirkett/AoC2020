import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]


compass = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
turns = {
    'L': {'E': 'N', 'S': 'E', 'W': 'S', 'N': 'W'},
    'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'},
    'F': {'N': 'N', 'E': 'E', 'S': 'S', 'W': 'W'}
}


def part1():
    facing = 'E'
    x, y = 0, 0
    for line in lines:
        inst = line[0]
        units = int(line[1:])
        if inst == 'L' or inst == 'R':
            for i in range(int(units / 90)):
                facing = turns[inst][facing]
        else:
            direction = compass[inst] if inst in compass else compass[turns[inst][facing]]
            x += units * direction[0]
            y += units * direction[1]
    return abs(x) + abs(y)


def rotate_points(x, y, deg, cw):
    for i in range(int(deg / 90)):
        ccw_factor = 1 if cw else -1
        x, y = [ccw_factor * c for c in [-y, x]]
    return x, y


def part2():
    waypoint_x, waypoint_y = 10, -1
    ship_x, ship_y = 0, 0
    for line in lines:
        inst = line[0]
        units = int(line[1:])
        if inst in compass:
            direction = compass[inst]
            waypoint_x += units * direction[0]
            waypoint_y += units * direction[1]
        elif inst == 'F':
            ship_x += units * waypoint_x
            ship_y += units * waypoint_y
        else:
            waypoint_x, waypoint_y = rotate_points(waypoint_x, waypoint_y, units, inst == 'R')
    return abs(ship_x) + abs(ship_y)

    
print(part1())
print(part2())
