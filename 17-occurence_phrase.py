def occurrence_caracteres(phrase: str):
    dico = {}
    for i in phrase:
        if i in dico:
            dico[i]+=1
        else:
            dico[i] = 1
    return dico



# tests

assert occurrence_caracteres("Bonjour à tous !") == {
    'B': 1, 'o': 3, 'n': 1, 'j': 1, 'u': 2, 'r': 1,
    ' ': 3, 'à': 1, 't': 1, 's': 1, '!': 1
}

assert occurrence_caracteres("ababbab") == {"a": 3, "b": 4}