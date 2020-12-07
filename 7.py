import fileinput

lines = [line.replace('\n', '').split(' contain ') for line in fileinput.input()]
rules = {k: v.replace('.', '').split(', ')for (k, v) in lines}


def part1(search_bag):
    search_bags = [search_bag]
    result_bags = []
    while len(search_bags):
        search_bag = search_bags.pop()
        for idx, line in enumerate(lines):
            if search_bag[:-1] in line[1]:
                search_bags.append(line[0])
                result_bags.append(line[0])
    return len(set(result_bags))


def get_contents(search_colour):
    if search_colour[-1:] != 's':
        search_colour += 's'
    contents = rules[search_colour]
    number_of_contents = 0
    for bag in contents:
        if bag == 'no other bags':
            continue
        number = int(bag[:1])
        colour = bag[2:]
        number_of_contents += number * (1 + get_contents(colour))
    return number_of_contents


def part2(search_bag):
    return get_contents(search_bag)


print(part1('shiny gold bag'))
print(part2('shiny gold bag'))