import copy


def ej1(n, b):
    if n < b:
        print(n, end='')
    else:
        res = n % b
        ej1(n // 5, b)
        print(res, end='')


def ej3_wrapper(mat):
    sol = copy.deepcopy(mat)
    ej3(mat, 0, sol)


def factible(sol, etapa, intento):
    for j in range(etapa):  # Filas
        if sol[etapa][j] == "T":
            return False
    for j in range(etapa):  # Columnas
        if sol[j][intento] == "T":
            return False
    return True


def print_sol(sol):
    for i in range(len(sol)):
        for j in range(len(sol[0])):
            print(sol[i][j], end=' ')
        print()
    print("*****************")


def ej2(m1, m2, sol, i_f, f_f, i_c, f_c, y):
    if i_f == f_f and i_c == f_c:
        for i in range(y):
            sol[i_f][i_c] += m1[i_f][i] * m2[i][i_c]
    else:
        if i_f < f_f:
            if i_c < f_c:
                m_f = (i_f + f_f) // 2
                m_c = (i_c + f_c) // 2
                ej2(m1, m2, sol, i_f, m_f, i_c, m_c, y)  # primer cuadrante
                ej2(m1, m2, sol, m_f + 1, f_f, i_c, m_c, y)  # 2º cuadrante

                ej2(m1, m2, sol, i_f, m_f, m_c + 1, f_c, y)  # 3er cuadrante
                ej2(m1, m2, sol, m_f + 1, f_f, m_c + 1, f_c, y)  # cuarto cuadrante
            else:  # solo 1 col
                m_f = (i_f + f_f) // 2
                ej2(m1, m2, sol, i_f, m_f, i_c, f_c, y)
                ej2(m1, m2, sol, m_f + 1, f_f, i_c, f_c, y)
        else:  # solo 1 fila
            m_c = (i_c + f_c) // 2
            ej2(m1, m2, sol, i_f, f_f, i_c, m_c, y)
            ej2(m1, m2, sol, i_f, f_f, m_c + 1, f_c, y)


def ej3(mat, etapa, sol):
    if etapa == len(mat):
        print_sol(sol)
    else:
        for i in range(len(mat)):
            if factible(sol, etapa, i):
                sol[etapa][i] = 1
                ej3(mat, etapa + 1, sol)
                sol[i][etapa] = 0


def ej32(mat, etapa):
    intento = 0
    while intento < len(mat[0]):
        if factible(mat, etapa, intento):
            mat[etapa][intento] = "T"
            if etapa == len(mat) - 1:
                print_sol(mat)
                print()
            else:
                ej32(mat, etapa + 1)
            mat[etapa][intento] = "X"
        intento += 1


m = [["X" for j in range(5)] for i in range(5)]
ej32(m, 0)

'''
# EJ 2
print("escriba filas m1")
x = int(input())  # filas m1

m1 = []
for i in range(x):
    m1_f = [int(j) for j in input().split()]
    m1.append(m1_f)
print("Filas:", len(m1), "Columnas:", len(m1[0]))
m2 = []
for i in range(len(m1[0])):
    m2_f = [int(j) for j in input().split()]
    m2.append(m2_f)
print("Filas:", len(m2), "Columnas:", len(m2[0]))

m3 = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
print(m3)
ej2(m1, m2, m3,0,len(m3),0,len(m3[0]),len(m1[0]))
'''
