def rendu(a_rendre):
    pieces_5 = a_rendre // 5
    a_rendre -= 5 * pieces_5

    pieces_2 = a_rendre // 2
    a_rendre -= 2 * pieces_2

    pieces_1 = a_rendre
    return (pieces_5, pieces_2, pieces_1)


# tests

assert tuple(rendu( 7)) == (1, 1, 0)
assert tuple(rendu(10)) == (2, 0, 0)
assert tuple(rendu(13)) == (2, 1, 1)
assert tuple(rendu(32)) == (6, 1, 0)
