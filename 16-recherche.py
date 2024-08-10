def recherche1(element, liste):
    for i in range(len(liste)):
        if liste[i] == element:
            return i

def recherche2(element, liste):
    id = liste[0]
    for i in range(len(liste)):
        if liste[i] == element:
            id = i
    return id
