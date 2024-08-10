def fibonacci(n):

    if n < 2:
        return n
    sequence = [0, 1]
    while len(sequence) < n+1:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[len(sequence)-1]






# tests

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(9) == 34
assert fibonacci(4) == 3