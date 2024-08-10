def est_trie(tableau):

    for index in range(1, len(tableau)):
        if tableau[index - 1] > tableau[index]:
            return False
        
    return True


# tests

assert     est_trie([0, 5, 8, 8, 9])
assert not est_trie([8, 12, 4])
assert     est_trie([-1, 4])
assert     est_trie([5])
assert     est_trie([])