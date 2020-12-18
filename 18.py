import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]


def find_matching_parenthesis(chars, pos):
    paren_positions = []
    for idx, char in enumerate(chars):
        if idx < pos:
            continue
        if char == '(':
            paren_positions.append(idx)
        elif char == ')':
            paren_positions.pop()
            if not len(paren_positions):
                return idx


def calculate(expression, add_first=False):
    while True:
        paren_pos = expression.find('(')
        if paren_pos == -1:
            break
        closing_paren_pos = find_matching_parenthesis(expression, paren_pos)
        subexp_result = calculate(expression[paren_pos+1:closing_paren_pos], add_first)
        expression = expression[:paren_pos] + str(subexp_result) + expression[closing_paren_pos+1:]

    if add_first:
        tokens = expression.split(' ')
        while True:
            try:
                plus_idx = tokens.index('+')
                result = int(tokens[plus_idx - 1]) + int(tokens[plus_idx + 1])
                tokens = tokens[:plus_idx - 1] + [str(result)] + tokens[plus_idx + 2:]
            except ValueError:
                break
        expression = ' '.join(tokens)

    tokens = expression.split(' ')
    result = tokens[0]
    current_op = ''
    for token in tokens[1:]:
        if token == '+' or token == '*':
            current_op = token
        else:
            result = eval(str(result) + current_op + token)

    return int(result)


def part1():
    return sum([calculate(line) for line in lines])


def part2():
    return sum([calculate(line, True) for line in lines])


print(part1())
print(part2())
