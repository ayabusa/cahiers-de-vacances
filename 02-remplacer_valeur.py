def remplacer(valeurs, valeur_cible, nouvelle_valeur):
    nv_tableau = []
    for i in range(len(valeurs)):
        if valeurs[i] == valeur_cible:
            nv_tableau.append(nouvelle_valeur)
        else:
            nv_tableau.append(valeurs[i])
    return nv_tableau


# Tests
# 1er test
valeurs = [3, 8, 7]
assert remplacer(valeurs, 3, 0) == [0, 8, 7]
assert valeurs == [3, 8, 7]
# 2nd test
valeurs = [3, 8, 3, 5]
assert remplacer(valeurs, 3, 0) == [0, 8, 0, 5]
assert valeurs == [3, 8, 3, 5]