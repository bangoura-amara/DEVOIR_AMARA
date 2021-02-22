# EXO 3:

def table_retour(valeur1, valeur2):
    table_retour = []

    for ama in valeur1 :
        if ama not in valeur2 :
            table_retour.append(ama)

        for ama in valeur2 :
            if ama not in valeur1 :
                table_retour.append(ama)

        return table_retour

result = table_retour([2, 4, 7, 8, 2], [1, 3, 9, 4, 6, 7])
print(result)