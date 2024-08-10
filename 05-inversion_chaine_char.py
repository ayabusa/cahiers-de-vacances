def inverser(mot):
    mot_inverse = ""
    for i in mot:
        mot_inverse = i + mot_inverse
    return mot_inverse

assert inverser("hello") == "olleh"