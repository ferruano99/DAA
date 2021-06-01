# Ej 2

def print_sol(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=' ')
        print()


def calcular_etapa(etapax, etapay, n):
    if etapay < (n - 1):
        return etapax, etapay + 1
    else:
        return etapax + 1, 0


# COMO EN EL ENUNCIADO
def bt_todas(M, etapax, etapay, n, sp_fila, sp_columna, sp_diagonal_izq, sp_diagonal_der, cte_magica, disponibles,
             n_sols):
    for intento in range(1, n * n + 1):
        if disponibles[intento - 1]:
            # PARTE FACTIBLE
            disponibles[intento - 1] = False
            M[etapax][etapay] = intento

            sp_fila[etapax] += intento
            sp_columna[etapay] += intento
            if etapax == etapay:
                sp_diagonal_izq += intento
            if etapax + etapay == n - 1:
                sp_diagonal_der += intento
            if sp_fila[etapax] <= cte_magica and sp_columna[etapay] <= cte_magica and sp_diagonal_izq <= cte_magica \
                    and sp_diagonal_der <= cte_magica:
                if etapax == n - 1 and etapay == n - 1:
                    if sum(sp_fila) == n * cte_magica and sum(
                            sp_columna) == n * cte_magica and sp_diagonal_izq == cte_magica \
                            and sp_diagonal_der == cte_magica:
                        print_sol(M)
                        print()
                        n_sols[0] += 1
                else:
                    nuevax, nuevay = calcular_etapa(etapax, etapay, n)
                    bt_todas(M, nuevax, nuevay, n, sp_fila, sp_columna, sp_diagonal_izq, sp_diagonal_der, cte_magica,
                             disponibles, n_sols)
            # DESMARCAMOS
            disponibles[intento - 1] = True

            sp_fila[etapax] -= intento
            sp_columna[etapay] -= intento
            if etapax == etapay:
                sp_diagonal_izq -= intento
            if etapax + etapay == (n - 1):
                sp_diagonal_der -= intento


def bt_wrapper(M, n, cte_magica):
    sp_fila = [0] * n
    sp_columna = [0] * n
    disponibles = [True] * (n * n)
    n_sols = [0]
    bt_todas(M, 0, 0, n, sp_fila, sp_columna, 0, 0, cte_magica, disponibles, n_sols)
    print(n_sols[0])


# TÉCNICA MÍA


def bt_magico(M, n, etapax, etapay, sp_fila, sp_columna, sp_dizq, sp_dder, cte_magica, disponibles):
    for intento in range(1, n * n):
        if disponibles[intento - 1]: # factible que es una línea
            disponibles[intento - 1] = False # marcamos soluciones
            M[etapax][etapay] = intento
            sp_fila[etapax] += intento
            sp_columna[etapay] += intento
            if etapax == etapay:
                sp_dizq += intento
            if etapax + etapay == n - 1:
                sp_dder += intento
            if etapax == n - 1 and etapay == n - 1 and sum(sp_fila) == (cte_magica * n) and sum(sp_columna) == (
                    cte_magica * n) \
                    and sp_dizq == cte_magica and sp_dder == cte_magica: # condición para imprimir
                print_sol(M)
                print()
            else:
                nuevax, nuevay = calcular_etapa(etapax, etapay, n)
                bt_magico(M, n, nuevax, nuevay, sp_fila, sp_columna, sp_dizq, sp_dder, cte_magica, disponibles) # BT
            # desmarcamos
            disponibles[intento - 1] = True
            sp_fila[etapax] -= intento
            sp_columna[etapay] -= intento
            if etapax == etapay:
                sp_dizq -= intento
            if etapax + etapay == n - 1:
                sp_dder -= intento


m = [[0 for j in range(3)] for i in range(3)]
n = len(m)
cte_magica = len(m) * ((len(m) ** 2 + 1) / 2)
bt_wrapper(m, n, cte_magica)
