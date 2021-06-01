def hanoi(origen, auxiliar, destino, n):
    if n == 1:
        print("Mueve disco", n, "desde torre", origen, "a torre", auxiliar)
        print("Mueve disco", n, "desde torre", auxiliar, "a torre", destino)
    else:
        hanoi(origen, auxiliar, destino, n - 1)
        print("Mueve disco", n, "desde torre", origen, "a torre", auxiliar)
        hanoi(destino, auxiliar, origen, n - 1)
        print("Mueve disco", n, "desde torre", auxiliar, "a torre", destino)
        hanoi(origen, auxiliar, destino, n - 1)


if __name__ == '__main__':
    n_discos = int(input())
    hanoi(1, 2, 3, n_discos)
