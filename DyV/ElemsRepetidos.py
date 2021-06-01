def mirar_numeros(elem):
    disponibles = [False] * 10
    while elem > 0:
        num = elem % 10
        disponibles[num] = True
        elem = elem // 10
    return disponibles

def dyv(a,inicio,fin,disponibles):
    if inicio == fin:
        return mirar_numeros(a[inicio])

    else:
        mitad = (inicio + fin) // 2
        d1 = dyv(a,inicio, mitad,disponibles)
        d2 = dyv(a, mitad + 1, fin,disponibles)
        disponibles2 = [False] * 10
        for i in range(len(disponibles2)):
            if d1[i] and d2[i]:
                disponibles2[i] = True
    return disponibles2



a = [2348, 1349, 7523, 3215]
elems = [False] * 10
print(dyv(a,0,len(a) - 1,elems))