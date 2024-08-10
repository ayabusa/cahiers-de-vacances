def occurrences_mini(donnees):
    id_min = []
    min = donnees[0]
    
    for i in range(len(donnees)):

        valeur = donnees[i]

        if valeur == min:
            id_min.append(i)
        elif valeur < min:
            min = valeur
            id_min = [i]

    return (min, id_min)


# tests

donnees = [+13, +49, +13, +5]
assert occurrences_mini(donnees) == (5, [3])

donnees = [-84, +75, -84, 0, +16]
assert occurrences_mini(donnees) == (-84, [0, 2])
