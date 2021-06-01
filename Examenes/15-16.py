def ej1(n):
    if n % 2 == 1:
        print("tiene impar")
    elif n < 10 and n % 2 != 1:
        print("no tiene impar")
    else:
        ej1(n // 10)


def ej2(a, inicio, fin):
    if inicio == fin:
        if a[inicio] % 2 == 0:
            return inicio
        else:
            return -1
    else:
        mitad = (inicio + fin) // 2
        if a[mitad] % 2 == 0:
            v1 = ej2(a, mitad + 1, fin)
            if v1 != -1:
                return v1
            else:
                return mitad
        else:
            v2 = ej2(a, inicio, mitad)
            if v2 != -1:
                return v2
            else:
                return -1


v = [2, 4, 8, 1, 3, -15, 3, 1, -3]
print(ej2(v, 0, len(v) - 1))
