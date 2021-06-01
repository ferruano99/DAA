# ej 2
import sys


def ej2(a, x):
    if x > a % 10:
        return a * 10 + x
    else:
        return a % 10 + 10 * ej2(a // 10, x)


def dyv(a, inicio, fin):
    mitad = (inicio + fin) // 2
    if mitad == a[mitad]:
        return mitad
    elif inicio >= fin:
        return -1
    elif mitad < a[mitad]:
        return dyv(a, inicio, mitad)
    else:
        return dyv(a, mitad + 1, fin)






def factible(a, s, etapa, suma_p, card_o, card_p, intento):
    if suma_p[0] + intento * a[etapa] > s:
        return False
    if card_p[0] > card_o[0]:
        return False
    return True

def ej3(a, s, etapa, suma_p, card_o, card_p, n_sol_o, disp, todas):
    intento = 0
    while intento < 2:
        if factible(a, s, etapa, suma_p, card_o, card_p, intento):
            disp[etapa] = a[etapa] * intento
            suma_p[0] += a[etapa] * intento
            if intento == 1:
                card_p[0] += 1
            if etapa == len(a) - 1:
                if s == suma_p[0]:
                    if card_p[0] < card_o[0]:
                        card_o[0] = card_p[0]
                        todas = [list(disp)]  # Me imprime la lista vacía
                        n_sol_o[0] = 1
                    elif card_p[0] == card_o[0]:
                        todas.append(list(disp))
                        n_sol_o[0] += 1
            else:
                todas = ej3(a, s, etapa + 1, suma_p, card_o, card_p, n_sol_o, disp,todas)
            suma_p[0] -= a[etapa] * intento
            disp[etapa] -= a[etapa] * intento
            if intento == 1:
                card_p[0] -= 1
        intento += 1
    return todas


a = [1, 2, 3, 5, 6, 7, 9]
s = 10
disp = [0] * len(a)
n_sol_o = [0]
todas = []
t = ej3(a, s, 0, [0], [sys.maxsize], [0], n_sol_o, disp,todas)
print(t)
print(n_sol_o)
