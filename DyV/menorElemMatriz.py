def menor_matriz(M, inicio_f, fin_f, inicio_c, fin_c):
    if inicio_f == fin_f and inicio_c == fin_c:
        return M[inicio_f][inicio_c]
    else:
        mitad_f = (inicio_f + fin_f) // 2
        mitad_c = (inicio_c + fin_c) // 2
        if inicio_f < fin_f:
            if inicio_c < fin_c: # VARIAS FILAS Y COLUMNAS
                m1 = menor_matriz(M, inicio_f, mitad_f, inicio_c, mitad_c)
                m2 = menor_matriz(M, mitad_f + 1, fin_f, mitad_c + 1, fin_c)
                m3 = menor_matriz(M, inicio_f, mitad_f, mitad_c + 1, fin_c)
                m4 = menor_matriz(M, mitad_f + 1, fin_f, inicio_c, mitad_c)
                return min(m1, m2, m3, m4)
            else:  # UNA COLUMNA
                m1 = menor_matriz(M, inicio_f, mitad_f, inicio_c, fin_c)
                m2 = menor_matriz(M, mitad_f + 1, fin_f, inicio_c, fin_c)
                return min(m1, m2)
        else:
            m1 = menor_matriz(M, inicio_f, fin_f, mitad_c + 1, fin_c)
            m2 = menor_matriz(M, inicio_f, fin_f, inicio_c, mitad_c)
            return min(m1, m2)


m = [
    [-11, 1, 2],
    [1, -5, 6],
    [2, 2, -1]
]
print(menor_matriz(m, 0, len(m) - 1, 0, len(m[0]) - 1))