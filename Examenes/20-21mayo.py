def factible(A, etapa, disponibles, sol, intento):
    if etapa == len(A) - 1:
        if not disponibles[intento]:
            return False
        if A[0][intento] == 0:
            return False
    else:
        if A[intento][sol[etapa - 1]] == 0:
            return False
        if not disponibles[intento]:
            return False
    return True


def ej1(A, etapa, disponibles, sol):
    exito = False
    intento = 1
    while intento < len(A) and not exito:
        if factible(A, etapa, disponibles, sol, intento):
            disponibles[intento] = False
            sol[etapa] = intento
            if etapa == len(A) - 1:
                exito = True
                sol[etapa + 1] = 0
            else:
                exito = ej1(A, etapa + 1, disponibles, sol)
                if not exito:
                    disponibles[intento] = True
                    sol[etapa] = -1
        intento += 1
    return exito


def ej2(a, x, ini, fin):
    if ini == fin:
        return ini, False
    else:
        mitad = (ini + fin) // 2
        v1, bool1 = ej2(a, x, 0, mitad)
        v2, bool2 = ej2(a, x, mitad + 1, fin)
        if x == v1 or x == v2:
            return 1, True
        elif v1 < x < v2:
            return 0, True
        else:
            if bool1:
                return v1, True
            elif bool2:
                return v2, True
            else:
                return -1, False


A = [[0, 1, 1, 0, 0],
     [1, 0, 1, 1, 1],
     [1, 1, 0, 1, 1],
     [0, 1, 1, 0, 1],
     [0, 1, 1, 1, 0]]
sol = [-1] * (len(A) + 1)
disponibles = [True] * len(A)
sol[0] = 0
e = ej1(A, 1, disponibles, sol)
if e:
    print(sol)

a = [0,1/27,2/27,3/27,6/27,7/27,8/27,9/27,18/27,19/27,20/27,21/27,24/27,25/27,26/27,1]
x = 0.05
print(ej2(a,x,0,len(a) - 1))
