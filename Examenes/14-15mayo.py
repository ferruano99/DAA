def ej2(v):
    v.sort()
    S = []
    for i in range(len(v) // 2):
        S.append((v[i], v[-i - 1]))
    return S


def ej3(v, min_e, i_f, f_f, i_c, f_c):
    if i_c == f_c and i_f == f_f:
        if v[i_f][i_c] < min_e:
            min_e = v[i_f][i_c]
    else:
        if i_f < f_f:
            if i_c < f_c:
                m_f = (i_f + f_f) // 2
                m_c = (i_c + f_c) // 2
                min_e = ej3(v, min_e, i_f, m_f, i_c, m_c)
                min_e = ej3(v, min_e, i_f, m_f, m_c + 1, f_c)

                min_e = ej3(v, min_e, m_f + 1, f_f, i_c, m_c)
                min_e = ej3(v, min_e, m_f + 1, f_f, m_c + 1, f_c)
            else:  # ic == fc
                m_f = (i_f + f_f) // 2
                min_e = ej3(v, min_e, i_f, m_f, i_c, f_c)
                min_e = ej3(v, min_e, m_f + 1, f_f, i_c, f_c)
        else:  # if == ff
            m_c = (i_c + f_c) // 2
            min_e = ej3(v, min_e, i_f, f_f, i_c, m_c)
            min_e = ej3(v, min_e, i_f, f_f, m_c + 1, f_c)
    return min_e


def factible(v, p, etapa, acumulados, s_acumulados, intento):
    if acumulados[etapa]:
        return False
    if s_acumulados + intento * v[etapa] > p:
        return False
    return True


def print_a(acumulados, a):
    v = []
    for i in range(len(a)):
        if acumulados[i]:
            v.append(a[i])
    print(v)


def ej4(v, n, p, etapa, acumulados, s_acumulados, s_opt):
    intento = 0
    while intento < 2:
        if factible(v, p, etapa, acumulados, s_acumulados, intento):
            s_acumulados += intento * v[etapa]
            if intento == 1:
                acumulados[etapa] = True
            if etapa == n:  # len array
                if s_opt[0] < s_acumulados:
                    s_opt[0] = s_acumulados
            else:
                ej4(v, n, p, etapa + 1, acumulados, s_acumulados, s_opt)
            s_acumulados -= intento * v[etapa]
            if intento == 1:
                acumulados[etapa] = False
        intento += 1
    return s_opt


v = [1, 6, 2, 7]

p = 4
acumulados = [False] * len(v)
s_opt = ej4(v, len(v) - 1, p, 0, acumulados, 0, [0])
print(s_opt)
