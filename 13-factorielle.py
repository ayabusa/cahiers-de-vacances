def factoriel(nombre):
    res = 1
    i = 1
    while i!=nombre:
        i+=1
        res = res*i
    return res


assert factoriel(7) == 5040