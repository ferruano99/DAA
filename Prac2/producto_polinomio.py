def print_polinomio(g, p):
    if len(p) == 1:
        if g == 0:
            if p[0] < 0:
                print(f" - {abs(p[0])}")
            else:
                print(f" + {p[0]}")
        else:
            if p[0] < 0:
                print(f" - {abs(p[0])}")
            elif p[0] > 0:
                print(f" + {p[0]}")
            else:
                print()
    else:
        if p[-1] < 0:
            print(f" - {abs(p[-1])}x^{len(p) - 1}", end='')
        elif p[-1] > 0:
            print(f" + {p[-1]}x^{len(p) - 1}", end='')
        print_polinomio(g, p[:-1])

def suma_p(p_p1, p_p2):
    if len(p_p1) == 0:
        return p_p2
    elif len(p_p2) == 0:
        return p_p1
    else:
        resultado = []
        resultado.append(p_p1[0] + p_p2[0])
        return resultado + suma_p(p_p1[1:], p_p2[1:])


def resta_p(p_p1, p_p2):
    if len(p_p1) == 0:
        for i in range(len(p_p2)):
            p_p2[i] *= -1
        return p_p2
    elif len(p_p2) == 0:
        return p_p1
    else:
        resultado = []
        resultado.append(p_p1[0] - p_p2[0])
        return resultado + resta_p(p_p1[1:], p_p2[1:])


def mult_m(p, m):
    aux = [0] * m
    aux.extend(p)
    p1 = aux
    return p1


def prod_p(p, q):  # concatenar m ceros al principio de la lsita en la primera parte
    if p == [0] or q == [0]:
        return [0]
    elif len(p) == 0:
        return q
    elif len(q) == 0:
        return p
    if len(q) == 1:
        aux = p.copy()
        for i in range(len(p)):
            aux[i] = q[0] * aux[i]
        return aux
    elif len(p) == 1:
        aux = q.copy()
        for i in range(len(q)):
            aux[i] = aux[i] * p[0]
        return aux
    else:
        m = min(len(p) // 2, len(q) // 2)  # cálculo de m
        pa = p[m:]
        pb = p[:m]
        qa = q[m:]
        qb = q[:m]
        paqax2m = mult_m(prod_p(pa, qa), m * 2)
        corchete = mult_m(corcho(pa, pb, qa, qb), m)
        pbqb = prod_p(pb, qb)
        resultado = suma_p(paqax2m, suma_p(corchete, pbqb))
        return resultado


def corcho(pa, pb, qa, qb):
    paypb = suma_p(pa, pb)
    qayqb = suma_p(qa, qb)
    mult = prod_p(paypb, qayqb)
    payqa = prod_p(pa, qa)
    pbyqb = prod_p(pb, qb)
    resta1 = resta_p(mult, payqa)
    resultado = resta_p(resta1, pbyqb)
    return resultado


if __name__ == '__main__':
    g_p1 = int(input())
    p_p1 = [int(i) for i in input().split()]
    g_p2 = int(input())
    p_p2 = [int(i) for i in input().split()]
    r = prod_p(p_p1, p_p2)
    print_polinomio(len(r) - 1, r)
