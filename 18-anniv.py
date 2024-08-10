def anniversaires(naissances: dict, mois):
    liste = []
    for keys in naissances:
        if naissances[keys] == mois:
            liste.append(keys)
    return liste

# Tests

assert sorted(anniversaires(dict(), 1)) == []
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 1)) == []
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 10)) == ['Nicolas']
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 7}, 7)) == ['Antoine', 'Camille']
assert sorted(anniversaires(
    {'Nicolas': 10, 'Antoine': 7, 'Camille': 11}, 13)) == []