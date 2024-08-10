
def tri_selection(tableau):
    n = len(tableau)
    for m in range(n):
        min_indice = trouver_indice_min(tableau, m)
        echanger_elements(tableau, min_indice, m)

def echanger_elements(tableau, x, y):
    tableau[x], tableau[y] = tableau[y], tableau[x]

def trouver_indice_min(tableau, debut):
    indice_min = debut
    for k in range(debut + 1, len(tableau)):
        if tableau[k] < tableau[indice_min]:
            indice_min = k
    return indice_min

# tests

tab = [1, 52, 6, -9, 12]
tri_selection(tab)
assert tab == [-9, 1, 6, 12, 52], "Exemple 1"

tab_vide = []
tri_selection(tab_vide)
assert tab_vide == [], "Exemple 2"

singleton = [9]
tri_selection(singleton)
assert singleton == [9], "Exemple 3"
