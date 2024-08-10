def inverser(mot):
    mot_inverse = ""
    for i in mot:
        mot_inverse = i + mot_inverse
    return mot_inverse

def est_palindrome(chaine):
    if chaine == inverser(chaine):
        return True
    else:
        return False

assert est_palindrome("bob") == True
assert est_palindrome("kayak") == True
assert est_palindrome("salut") == False