def correspond(mot_complet, mot_a_trous):
    if len(mot_complet) != len(mot_a_trous):

        return False
    
    for i in range(len(mot_complet)):

        if (mot_a_trous[i] != '.') and (mot_a_trous[i] != mot_complet[i]):
            return False
        
    return True

# tests

assert correspond("INFORMATIQUE", "INFO.MA.IQUE") == True
assert correspond("AUTOMATIQUE", "INFO.MA.IQUE") == False
assert correspond("INFO", "INFO.MA.IQUE") == False
assert correspond("INFORMATIQUES", "INFO.MA.IQUE") == False