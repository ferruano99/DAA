'''MÉTODOS PARA CREAR MATRICES'''


def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print()


def crear_matriz(filas, cols):
    sol = [[0 for j in range(cols)] for i in range(filas)]
    return sol


def mayoritario(v, inicio, fin, mayor):
    if inicio == fin:
        mayor = v[inicio]
        return True
    else:
        existe = False
        mitad = (inicio + fin) // 2
        mayor1 = -1
        mayor2 = -1
        existe1 = mayoritario(v, inicio, mitad, mayor1)
        existe2 = mayoritario(v, mitad + 1, fin, mayor2)
        if existe1:
            existe = comprobar_mayoritario(v, mayor1, inicio, fin)
            if existe:
                mayor = mayor1
        if not existe and existe2:
            existe = comprobar_mayoritario(v, mayor2, inicio, fin)
            if existe:
                mayor = mayor2
        return existe


def comprobar_mayoritario(v, mayor, inicio, fin):
    veces = 0
    for i in range(inicio, fin + 1):
        if v[i] == mayor:
            veces += 1
    return veces > (fin - inicio + 1) // 2


'''
n_reinas:
Tablero de 9x9
op1: ir rellenando el tablero donde queramos poner la reina
op2 tener un vector que nos diga dónde está cada reina
'''


def factible_nreinas(sol, etapa, intento):
    for i in range(etapa):
        if "R" == sol[etapa][i]:
            return False
    for i in range(etapa):
        if "R" == sol[i][intento]:
            return False
    dEtapa = etapa - 1
    dIntento = intento - 1
    while dEtapa >= 0 and dIntento >= 0:  # diagonal izq
        if sol[dEtapa][dIntento] == "R":
            return False
        dEtapa -= 1
        dIntento -= 1
    dEtapa = etapa - 1
    dIntento = intento + 1
    while dEtapa >= 0 and dIntento < len(sol):  # diag der
        if sol[dEtapa][dIntento] == "R":
            return False
        dEtapa -= 1
        dIntento += 1
    return True


def bt_nreinas_1sol(sol, etapa):
    exito = False
    intento = 0
    while intento < len(sol) and not exito:
        if factible_nreinas(sol, etapa, intento):
            # marcamos
            sol[etapa][intento] = "R"
            if etapa == (len(sol) - 1):
                exito = True
            else:
                exito = bt_nreinas_1sol(sol, etapa + 1)
                if not exito:
                    sol[etapa][intento] = "X"
        intento += 1
    return exito


def bt_nreinas_todas(sol, etapa, n_sol):  # que cuenta las sols
    intento = 0
    while intento < len(sol):
        if factible_nreinas(sol, etapa, intento):
            # marcamos
            sol[etapa][intento] = "R"
            if etapa == (len(sol) - 1):
                print()
                n_sol[0] += 1
                print_m(sol)
            else:
                bt_nreinas_todas(sol, etapa + 1, n_sol)
            sol[etapa][intento] = "X"
        intento += 1


''' EJERCICIO SOCIOS '''


# NO EFICIENTE
def factible_socios(cosas, sol, etapa, intento):
    total_cosas = 0
    for i in cosas:
        total_cosas += i
    mitades = total_cosas // 2
    mi_socio = 0
    for i in range(etapa):  # vemos el peso que tenemos
        if sol[i] == intento:
            mi_socio += cosas[i]
    if (mi_socio + cosas[etapa]) > mitades:
        return False
    return True


def bt_socios_1sol(cosas, sol, etapa):
    exito = False
    intento = 1
    while intento <= 2 and not exito:
        if factible_socios(cosas, sol, etapa, intento):
            sol[etapa] = intento
            if etapa == (len(sol) - 1):
                exito = True
            else:
                exito = bt_socios_1sol(cosas, sol, etapa + 1)
                if not exito:
                    sol[etapa] = 0
        intento += 1
    return exito


def bt_socios_todas(cosas, sol, etapa):
    intento = 1
    while intento <= 2:
        if factible_socios(cosas, sol, etapa, intento):
            sol[etapa] = intento
            if etapa == (len(sol) - 1):
                print(sol)
            else:
                bt_socios_todas(cosas, sol, etapa + 1)
            sol[etapa] = 0
        intento += 1


''' SALTO DEL CABALLO 
array relativo de movimientos:
    especificamos cómo se tiene que mover el caballo

    '''


def factible_caballo(mat, nuevax, nuevay):
    if 0 > nuevax:
        return False
    if len(mat) <= nuevax:
        return False
    if 0 > nuevay:
        return False
    if len(mat[0]) <= nuevay:
        return False
    if mat[nuevax][nuevay] != 0:
        return False
    return True


def bt_saltocaballo_1sol(mat, etapax, etapay, movX, movY, pos):
    exito = False
    intento = 0
    while intento < len(movX) and not exito:
        nuevax = etapax + movX[intento]
        nuevay = etapay + movY[intento]
        if factible_caballo(mat, nuevax, nuevay):
            mat[nuevax][nuevay] = pos
            if pos == (len(mat) * len(mat[0])):
                exito = True
            else:
                exito = bt_saltocaballo_1sol(mat, nuevax, nuevay, movX, movY, pos + 1)
                if not exito:
                    mat[nuevax][nuevay] = 0
        intento += 1
    return exito


def bt_saltocaballo_todas(mat, etapax, etapay, movX, movY, pos, n_soluciones):
    intento = 0
    while intento < len(movX):
        nuevax = etapax + movX[intento]
        nuevay = etapay + movY[intento]
        if factible_caballo(mat, nuevax, nuevay):
            mat[nuevax][nuevay] = pos
            if pos == (len(mat) * len(mat[0])):
                n_soluciones[0] += 1
                print()
                print_m(mat)
            else:
                bt_saltocaballo_todas(mat, nuevax, nuevay, movX, movY, pos + 1, n_soluciones)
            mat[nuevax][nuevay] = 0
        intento += 1


''' SUDOKU '''


def factible_sudoku(mat, etapax, etapay, intento):
    for i in range(etapax):  # filas
        if mat[i][etapay] == intento:
            return False
    for i in range(etapay):
        if mat[etapax][i] == intento:
            return False
    cuadrantex = etapax // 3
    cuadrantey = etapay // 3
    for i in range(cuadrantex * 3, cuadrantex * 3 + 3):
        for j in range(cuadrantey * 3, cuadrantey * 3 + 3):
            if mat[i][j] == intento:
                return False
    return True


'''    for i in range(len(mat[0])): # columnas
        if mat[etapax][i] == intento:
            return False'''


def calcularpos(etapax, etapay, mat):
    if etapay == len(mat) - 1:  # filas son igual a la distancia
        return etapax + 1, 0
    else:
        return etapax, etapay + 1


def bt_sudoku_1sol(mat, etapax, etapay):
    exito = False
    if mat[etapax][etapay] != 0:
        if etapax == len(mat) - 1 and etapay == len(mat) - 1:
            exito = True
        else:
            (nuevax, nuevay) = calcularpos(etapax, etapay, mat)
            exito = bt_sudoku_1sol(mat, nuevax, nuevay)
    else:
        intento = 1
        while intento < 10 and not exito:
            if factible_sudoku(mat, etapax, etapay, intento):
                mat[etapax][etapay] = intento
                if etapay == len(mat) - 1 and etapax == len(mat[0]) - 1:
                    exito = True
                else:
                    nuevax, nuevay = calcularpos(etapax, etapay, mat)
                    exito = bt_sudoku_1sol(mat, nuevax, nuevay)
                    if not exito:
                        mat[nuevax][nuevay] = 0
            intento += 1
    return exito


def bt_sudoku_nsols(mat, etapax, etapay):
    if mat[etapax][etapay] != 0:
        if etapax == len(mat) - 1 and etapay == len(mat) - 1:
            print_m(mat)
            print()
        else:
            (nuevax, nuevay) = calcularpos(etapax, etapay, mat)
            bt_sudoku_nsols(mat, nuevax, nuevay)
    else:
        intento = 1
        while intento < 10:
            if factible_sudoku(mat, etapax, etapay, intento):
                mat[etapax][etapay] = intento
                if etapay == len(mat) - 1 and etapax == len(mat[0]) - 1:
                    print_m(mat)
                    print()
                else:
                    nuevax, nuevay = calcularpos(etapax, etapay, mat)
                    bt_sudoku_nsols(mat, nuevax, nuevay)
                mat[etapax][etapay] = 0
            intento += 1


''' PROBLEMA DEL LABERINTO'''


def factible_laberinto(tablero, nuevax, nuevay, movx, movy, intento):
    if nuevax < 0:
        return False
    if nuevay < 0:
        return False
    if nuevax >= len(tablero):
        return False
    if nuevay >= len(tablero):
        return False
    if tablero[nuevax][nuevay] == "M":
        return False
    if tablero[nuevax][nuevay] == "X":
        return False
    return True


def bt_laberinto_1sol(tablero, etapax, etapay, movx, movy):  # Mal no sé por qué
    exito = False
    intento = 0
    while intento < len(movx) and not exito:
        nuevax = etapax + movx[intento]
        nuevay = etapay + movy[intento]
        if factible_laberinto(tablero, nuevax, nuevay, movx, movy, intento):
            if tablero[nuevax][nuevay] == " ":
                tablero[nuevax][nuevay] = "X"
            if tablero[nuevax][nuevay] == "S":
                exito = True
            else:
                exito = bt_laberinto_1sol(tablero, nuevax, nuevay, movx, movy)
                if not exito:
                    tablero[nuevax][nuevay] = " "
        intento += 1
    return exito


# CUADRADO MÁGICO (óptimo)

def bt_cuadradomagico_todas(M, etapax, etapay, disponibles, sp_filas, sp_columnas, sp_diagizq, sp_diagder, n_magico):
    intento = 1
    while intento <= len(M) * len(M):
        if disponibles[intento - 1]:
            M[etapax][etapay] = intento
            disponibles[intento - 1] = False
            sp_filas[etapax] += intento
            sp_columnas[etapay] += intento
            if etapax == etapay:
                sp_diagizq += intento
            if etapax + etapay == len(M) - 1:
                sp_diagder += intento
            if sp_filas[etapax] <= n_magico and sp_columnas[etapay] <= \
                    n_magico and sp_diagizq <= n_magico \
                    and sp_diagder <= n_magico:
                if etapax == len(M) - 1 and etapay == len(M) - 1:
                    print_m(M)
                    print()
                else:
                    nuevax, nuevay = calcularpos(etapax, etapay, M)
                    bt_cuadradomagico_todas(M, nuevax, nuevay, disponibles, sp_filas, sp_columnas, sp_diagizq,
                                            sp_diagder, n_magico)
            M[etapax][etapay] = 0
            disponibles[intento - 1] = True
            sp_filas[etapax] -= intento
            sp_columnas[etapay] -= intento
            if etapax == etapay:
                sp_diagizq -= intento
            if etapax + etapay == len(M) - 1:
                sp_diagder -= intento
        intento += 1


''' PERMUTACIONES'''


def bt_permconrep(a, r, etapa, sol):
    exito = False
    intento = 0
    while intento < len(a):
        if r[intento] > 0:
            sol[etapa] = a[intento]
            r[intento] -= 1
            if etapa == len(sol) - 1:
                exito = True
            else:
                exito = bt_permconrep(a, r, etapa + 1, sol)
                if not exito:
                    r[intento] += 1
                    sol[etapa] = None
        intento += 1
    return exito


def bt_permconrep_todas(a, r, etapa, sol, contador):
    intento = 0
    while intento < len(a):
        if r[intento] > 0:
            sol[etapa] = a[intento]
            r[intento] -= 1
            if etapa == len(sol) - 1:
                print(sol)
                contador[0] += 1
            else:
                bt_permconrep_todas(a, r, etapa + 1, sol, contador)
            r[intento] += 1
            sol[etapa] = None
        intento += 1


''' DIVIDES '''


# MAYOR Y MENOR ELEMENTO DE UN VECTOR
def divide_mayormenor(A, inicio, final):
    if inicio == final:
        return A[inicio], A[final]
    else:
        mitad = (inicio + final) // 2
        max1, min1 = divide_mayormenor(A, inicio, mitad)
        max2, min2 = divide_mayormenor(A, mitad + 1, final)
        maxim = max(max1, max2)
        minim = min(min1, min2)
        return maxim, minim


# Número que más veces se repite en un array

def mayoritario_elem(A, inicio, final):
    if inicio == final:
        return True, A[inicio]
    else:
        mitad = (inicio + final) // 2
        mayoritario_elem(A, inicio, mitad)
        mayoritario_elem(A, mitad + 1, final)


# VER SI UN NÚMERO ESTÁ REPETIDO EN TODOS LOS ELEMNETOS DE UNA LISTA (se devuelve una lista de booleanos del 10 elementos)


def ver_repetidos(vector, esta, inicio):
    nuevoesta = list(esta)
    numeros_vector = vector[inicio]
    while numeros_vector > 0:
        numero = numeros_vector % 10
        nuevoesta[numero] = True
        numeros_vector = numeros_vector // 10

    return nuevoesta


def comparar_listas(izq, der):
    l_indices = [False] * 10
    for i in range(len(izq)):
        if izq[i] and der[i]:
            l_indices[i] = True
    return l_indices


def esta_repetido(vector, esta, inicio, final):
    if inicio == final:
        nuevoesta = ver_repetidos(vector, esta, inicio)
        return nuevoesta
    else:
        mitad = (inicio + final) // 2
        nuevoestader = esta_repetido(vector, esta, inicio, mitad)
        nuevoestaizq = esta_repetido(vector, esta, mitad + 1, final)
        lista = comparar_listas(nuevoestaizq, nuevoestader)
        return lista


# MERGESORT

def mergesort(a, inicio, fin):
    if inicio == fin:
        return [a[inicio]]
    else:
        mitad = (inicio + fin) // 2
        mitadi = mergesort(a, inicio, mitad)
        mitadd = mergesort(a, mitad + 1, fin)
        sol = []
        i = 0
        j = 0
        while i < len(mitadi) and j < len(mitadd):
            if mitadi[i] < mitadd[j]:
                sol.append(mitadi[i])
                i += 1
            else:
                sol.append(mitadd[j])
                j += 1
        while i < len(mitadi):
            sol.append(mitadi[i])
            i += 1
        while j < len(mitadd):
            sol.append(mitadd[j])
            j += 1
        return sol


# Último elemento par de un vector O(logn) (solo 1 llamada)
def ultimo_par(a, inicio, fin):
    if inicio == fin:
        return inicio
    else:
        mitad = (inicio + fin) // 2
        if a[mitad] % 2 == 0:
            vi = ultimo_par(a, mitad + 1, fin)
            if vi % 2 == 0:
                return vi
            else:
                return -1
        else:
            vd = ultimo_par(a, inicio, mitad)
            if vd % 2 == 0:
                return vd
            else:
                return -1


def ultimo_par2(a, ini, fin):
    if ini == fin:
        return ini
    else:
        mitad = (ini + fin) // 2
        if a[mitad] % 2 == 0:
            fin = len(a)
            v1 = ultimo_par2(a, mitad + 1, fin)
            if v1 % 2 == 0:
                return v1
            else:
                return mitad
        else:
            v2 = ultimo_par2(a, ini, mitad)
            if v2 % 2 == 0:
                return v2
            else:
                return -1


m = crear_matriz(3, 3)
sp_filas = [0] * len(m)
sp_cols = [0] * len(m[0])

bt_cuadradomagico_todas(m, 0, 0, [True] * (len(m) * len(m)), sp_filas, sp_cols, 0, 0, len(m) * ((len(m) ** 2 + 1) // 2))
'''

PARÁMETROS DE ENTRADA PARA SALTO DE CABALLO

mat = crear_matriz(5, 5)
# Array de posiciones relativas
# primero decimos que el caballo está en el medio y luego array
n_soluciones = [0]
mat[2][2] = 1
movX = [1, 2, -1, -2, 1, 2, -1, -2]
movY = [2, 1, -2, -1, -2, -1, 2, 1]
bt_saltocaballo_todas(mat, 2, 2, movX, movY, 2, n_soluciones)
print(n_soluciones[0])
'''
