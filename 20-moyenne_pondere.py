def moyenne(notes_ponderees):
    somme_ponderee = 0.0
    somme_coefficients = 0

    for note, coefficient in notes_ponderees:
        somme_ponderee += coefficient * note
        somme_coefficients += coefficient

    return somme_ponderee / somme_coefficients

# tests

def sont_proches(x, y):
    "Renvoie un booléen : les nombres x et y sont-ils proches ?"
    return abs(x - y) < 10**-6

assert sont_proches(moyenne([(15.0, 2)]), 15.0)
assert sont_proches(moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]), 12.5)