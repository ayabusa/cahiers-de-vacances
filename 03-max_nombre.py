def maximum(nombres):
    max = nombres[0]
    for i in range(len(nombres)):
        if max < nombres[i]:
            max = nombres[i]
    return max


# Tests
assert maximum([98, 12, 104, 23, 131, 9]) == 131
assert maximum([-27, 24, -3, 15]) == 24