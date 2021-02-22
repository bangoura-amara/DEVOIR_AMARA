# EXO 2:

def chaine_caractere():
    chaie1 = "alpha"
    chaie2 = "mamadou"
    m = ""
    for x in chaie1:
        for y in chaie2:
            while x == y:
                m = y
                break
    print(m)

chaine_caractere()

def chaie_carac(chaie1 = "klbc", chaie2 = "kaba"):
    pecos = []
    for a in chaie1 :
        for b in chaie2 :
            if a == b :
                if a not in pecos:
                    pecos.append(a)
    print(pecos)
    return pecos
chaie_carac()