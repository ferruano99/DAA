import copy
import math


def mult_m(m1, m2):
    m3 = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]  # Filas de m1 x columnas de m2
    acc = 0
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                acc += m1[i][k] * m2[k][j]
            m3[i][j] = acc
            acc = 0
    return m3


def m_por_cte(cte, m):
    m3 = copy.deepcopy(m)
    for i in range(len(m3)):
        for j in range(len(m3[0])):
            m3[i][j] = cte * m[i][j]
    return m3


def resta_m(m1, m2):
    m3 = copy.deepcopy(m1)
    for i in range(len(m3)):
        for j in range(len(m3[0])):
            m3[i][j] -= m2[i][j]
    return m3


def gradiente(n, At, A, x, b):
    dosAt = m_por_cte(n, At)  # 2At
    porA = mult_m(dosAt, A)  # 2AtA
    porx = mult_m(porA, x)  # 2AtAx
    otraparte = mult_m(m_por_cte(n, At), b)  # 2Atb
    gradiente = resta_m(porx, otraparte)  # 2AtAx - 2Atb
    return gradiente


def modulo(g):
    x = 0
    for i in range(len(g)):
        x += math.pow(g[i][0], 2)
    return math.sqrt(x)


def algoritmo_voraz_descenso_gradiente(A, At, b, x0, alfa, epsilon):
    x = x0  # x <- x0
    g = gradiente(2, At, A, x, b)  # g <- 2AtAx - ́2Atb
    while modulo(g) > epsilon:  # |g| > epsilon
        x = resta_m(x, m_por_cte(alfa, g))  # x <- x - alfa*g
        g = gradiente(2, At, A, x, b)  # g <- 2AtAx - ́2Atb
    print_result(x)  # return x


def print_result(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print("{:.4f}".format(x[i][j]), end=' ')
    print()


An, Am = input().split()
An = int(An)
Am = int(Am)
A = []
for i in range(An):
    Afila = [float(j) for j in input().split()]
    A.append(Afila)
b = [[float(i)] for i in input().split()]
x0 = [[float(i)] for i in input().split()]
alfa = float(input())
epsilon = float(input())
At = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]  # Cálculo de la traspuesta de A
algoritmo_voraz_descenso_gradiente(A, At, b, x0, alfa, epsilon)
