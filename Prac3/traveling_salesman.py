import math
import sys


def traveling_wrapper(arr, distances):
    partial_arr = [-1] * len(arr)
    partial_arr[0] = 0
    returns = traveling(arr, distances, partial_arr, sys.maxsize, 1, [], 0)
    print("{:.4f}".format(returns[0]))
    for q in range(len(returns[1]) - 1):
        print(returns[1][q], end=' ')
    print(returns[1][-1])


def traveling(arr, distances, arr_sol, acc_opt, step, arr_opt, acc):
    if step > 1:  # Primera condición de poda
        acc += distances[arr_sol[step - 1]][0]
    if acc < acc_opt:  # Condición de optimalidad y poda (minimizamos el coste)
        if step == len(arr):  # Última iteración de la solución parcial
            acc_opt = acc
            arr_opt = arr_sol.copy()
            acc -= distances[arr_sol[-1]][0]
        else:  # Backtracking
            if step > 1:
                acc -= distances[arr_sol[step - 1]][0]
            for k in range(len(arr)):
                if k not in arr_sol:
                    arr_sol[step] = k
                    acc += distances[arr_sol[step]][arr_sol[step - 1]]
                    if acc < acc_opt:
                        acc_opt, arr_opt = traveling(arr, distances, arr_sol, acc_opt, step + 1, arr_opt, acc)
                    acc -= distances[arr_sol[step]][arr_sol[step - 1]]  # Desmarcamos las soluciones
                    arr_sol[step] = -1
    return acc_opt, arr_opt


def euclidean_distance(q, p):
    return math.sqrt(math.pow((q[0] - p[0]), 2) + math.pow((q[1] - p[1]), 2))


n = int(input())
arr = []
for i in range(n):
    n1, n2 = input().split(" ")
    arr.append((float(n1), float(n2)))
matrix = []
for i in range(len(arr)):  # Array para el cálculo de todas las distancias (ahorro en eficiencia)
    ls_aux = []
    for j in range(len(arr)):
        ls_aux.append(euclidean_distance(arr[j], arr[i]))
    matrix.append(ls_aux)
traveling_wrapper(arr, matrix)
