def indice_min(nombres) -> int:
    min = (0,nombres[0])
    for i in range(len(nombres)):
        if nombres[i] < min[1]:
            min = (i, nombres[i])
    return min[0]



# tests

assert indice_min([5]) == 0
assert indice_min([2, 4, 1, 1]) == 2
assert indice_min([5, 3, 2, 5, 2]) == 2