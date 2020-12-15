inputs = 2, 0, 1, 9, 5, 19
numbers = {v: k for k, v in enumerate(inputs)}


def run(limit):
    run_numbers = numbers.copy()
    current = 0
    for i in range(len(run_numbers), limit):
        last_seen = run_numbers.get(current, i)
        run_numbers[current] = i
        if i == limit - 1:
            return current
        current = i - last_seen


print(run(2020))
print(run(30000000))
