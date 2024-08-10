def multiplication(a, b):
    positif = True
    if (a<0 and b>0) or (a>0 and b<0):
        positif = False
    produit = 0
    for i in range(abs(a)):
        produit+=abs(b)
    if positif:
        return produit
    else:
        return -produit


# Tests
assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(3, -4) == -12
assert multiplication(-2, 0) == 0
