def valeur_et_indice_du_max(valeurs):
        
    if valeurs != []:
        valeur_max = valeurs[0]
        id_max = 0

        for i in range(1, len(valeurs)):
            j = valeurs[i]

            if j > valeur_max:
                valeur_max = j
                id_max = i

        return (valeur_max, id_max)
    
    
    else:
        return (None, None)


# tests
assert valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert valeur_et_indice_du_max([1, 1, 1, 99, 99]) == (99, 3)
assert valeur_et_indice_du_max([10]) == (10, 0)
assert valeur_et_indice_du_max([]) == (None, None)
