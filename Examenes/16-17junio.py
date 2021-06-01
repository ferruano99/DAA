# EJERCICIO 1
def ver_repetidos(vector, esta,inicio):
    nuevoesta = list(esta)
    numeros_vector = vector[inicio]
    while numeros_vector > 0:
        numero = numeros_vector % 10
        nuevoesta[numero] = True
        numeros_vector = numeros_vector // 10

    return nuevoesta

def comparar_listas(izq,der):
    l_indices = [False] * 10
    for i in range(len(izq)):
        if izq[i] and der[i]:
            l_indices[i] = True
    return l_indices



def esta_repetido(vector,esta,inicio,final):
    if inicio == final:
        nuevoesta = ver_repetidos(vector,esta,inicio)
        return nuevoesta
    else:
        mitad = (inicio + final) // 2
        nuevoestader = esta_repetido(vector,esta,inicio,mitad)
        nuevoestaizq = esta_repetido(vector,esta,mitad + 1,final)
        lista = comparar_listas(nuevoestaizq,nuevoestader)
        return lista



# EJERCICIO 3
def factible(S, sol, etapa, intento, half):
    acc = 0
    for i in range(etapa):
        if sol[i] == intento:
            acc += S[i]
    if acc + etapa > half:
        return False
    return True


def print_sol(sol,S):
    A = []
    B = []
    for i in range(len(sol)):
        if sol[i] == 0:
            A.append(S[i])
        else:
            B.append(S[i])
    print(A)
    print(B)
    print()


def ej3(S, sol, etapa, half):
    intento = 0
    while intento < 2:
        if factible(S, sol, etapa, intento, half):
            sol[etapa] = intento
            if etapa == len(sol) - 1:
                print_sol(sol,S)
            else:
                ej3(S, sol, etapa + 1, half)
            sol[etapa] = -1
        intento += 1






