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


if __name__ == '__main__':
    g_p1 = int(input())
    p_p1 = [int(i) for i in input().split()]
    g_p2 = int(input())
    p_p2 = [int(i) for i in input().split()]
    p_suma = suma_p(p_p1, p_p2)
    p_resta = resta_p(p_p1, p_p2)
    print_polinomio(len(p_suma) - 1, p_suma)
    print_polinomio(len(p_resta) - 1, p_resta)
