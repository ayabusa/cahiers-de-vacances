def derniere_occurrence(tableau, cible):
    der_oc = len(tableau)
    for i in range(len(tableau)):
        if tableau[i] == cible:
            der_oc = i
    return der_oc

# tests

assert derniere_occurrence([5, 3], 1) == 2
assert derniere_occurrence([2, 4], 2) == 0
assert derniere_occurrence([2, 3, 5, 2, 4], 2) == 3