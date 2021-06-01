def factible(m, etapax, etapay, sp_filas, sp_cols, disponibles, sp_diagi, sp_diagd, n_magico, intento):
    if not disponibles[intento - 1]:
        return False
    if intento + sp_filas[etapax] > n_magico and intento + sp_cols[etapay] > n_magico:
        return False
    if etapax == etapay:
        if sp_diagi + intento > n_magico:
            return False
    if etapax + etapay == len(m) - 1:
        if sp_diagd + intento > n_magico:
            return False
    return True


def calcular_etapa(etapax, etapay, m):
    if etapay >= len(m) - 1:
        return etapax + 1, 0
    else:
        return etapax, etapay + 1


def bt(m, etapax, etapay, sp_filas, sp_cols, disponibles, sp_diagi, sp_diagd, n_magico):
    exito = False
    intento = 1
    while intento <= (len(m) * len(m[0])):
        if factible(m, etapax, etapay, sp_filas, sp_cols, disponibles, sp_diagi, sp_diagd, n_magico, intento):
            m[etapax][etapay] = intento

            disponibles[intento - 1] = False
            sp_filas[etapax] += intento
            sp_cols[etapay] += intento
            if etapax == etapay:
                sp_diagi += intento
            if etapax + etapay == len(m) - 1:
                sp_diagd += intento
            if etapax == len(m) - 1 and etapay == len(m) - 1:
                if sum(sp_filas) == len(m) * n_magico and sum(sp_cols) == len(m) * n_magico and \
                        sp_diagi == n_magico and sp_diagd == n_magico:
                    exito = True
            else:
                nuevax, nuevay = calcular_etapa(etapax, etapay, m)
                exito = bt(m, nuevax, nuevay, sp_filas, sp_cols, disponibles, sp_diagi, sp_diagd, n_magico)
                if not exito:
                    sp_filas[etapax] -= intento
                    sp_cols[etapay] -= intento
                    disponibles[intento - 1] = True
                    if etapax == etapay:
                        sp_diagi -= intento
                    if etapax + etapay == len(m) - 1:
                        sp_diagd -= intento
        intento += 1
    return exito


m = [[0 for j in range(4)] for i in range(4)]
sp_filas = [0] * len(m)
sp_cols = [0] * len(m[0])
disponibles = [True] * (len(m) * len(m[0]))  # 0 al 9

exito = bt(m, 0, 0, sp_filas, sp_cols, disponibles, 0, 0, len(m) * ((len(m) ** 2 + 1) / 2))
if exito:
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end="    ")
        print()
else:
    print("nada")
