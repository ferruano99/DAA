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


if __name__ == '__main__':
    grado = int(input())
    polinomio = [int(i) for i in input().split()]
    print_polinomio(grado, polinomio)
