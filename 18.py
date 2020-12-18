import fileinput

lines = [line.replace('\n', '') for line in fileinput.input()]


def find_matching_parenthesis(tokens, pos):
    paren_positions = []
    for idx, token in enumerate(tokens):
        if idx < pos:
            continue
        if token == '(':
            paren_positions.append(idx)
        elif token == ')':
            paren_positions.pop()
            if not len(paren_positions):
                return idx


def calculate(expression, add_first=False):
    expression = expression.replace('(', '( ').replace(')', ' )')
    tokens = expression.strip().split(' ')
    while True:
        try:
            paren_idx = tokens.index('(')
            closing_paren_idx = find_matching_parenthesis(tokens, paren_idx)
            subexp = ' '.join(tokens[paren_idx+1:closing_paren_idx])
            subexp_result = calculate(subexp, add_first)
            tokens = tokens[:paren_idx] + [str(subexp_result)] + tokens[closing_paren_idx + 1:]
        except ValueError:
            break

    if add_first:
        while True:
            try:
                plus_idx = tokens.index('+')
                result = int(tokens[plus_idx - 1]) + int(tokens[plus_idx + 1])
                tokens = tokens[:plus_idx - 1] + [str(result)] + tokens[plus_idx + 2:]
            except ValueError:
                break

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
