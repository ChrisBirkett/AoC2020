inputs = 2, 0, 1, 9, 5, 19
original_numbers = {v: k for k, v in enumerate(inputs)}


def run(limit):
    numbers = original_numbers.copy()
    current = 0
    for i in range(len(numbers), limit):
        last_seen = numbers.get(current, i)
        numbers[current] = i
        if i < limit - 1:
            current = i - last_seen
    return current


print(run(2020))
print(run(30000000))
