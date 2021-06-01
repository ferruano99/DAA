def dyv(a, ini, fin):
    if ini == fin:
        if a[ini] == ini:
            return ini
        else:
            return -1
    else:
        mitad = (ini + fin) // 2
        if mitad <= a[mitad]:
            v1 = dyv(a, ini, mitad)
            if v1 != -1:
                return v1
            else:
                return mitad
        else:
            v2 = dyv(a, mitad + 1, fin)
            return v2


a = [0, 1, 2, 5, 7]
print(dyv(a, 0, len(a) - 1))
