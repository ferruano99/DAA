def recursive_activity_selector(arr):
    n = len(arr)
    A = [arr[0]]
    k = 0
    for m in range(1, n):
        if arr[m][0] >= arr[k][1]:
            A.append(arr[m])
            k = m
    return A


n = int(input())
ci = [int(i) for i in input().split()]
fi = [int(i) for i in input().split()]
arr_acts = []
for i in range(n):
    actividad = (ci[i], fi[i])  # Cogemos inicio de tarea con fin en una tupla
    arr_acts.append(actividad)
arr = sorted(arr_acts, key=lambda x: x[1])  # Ordenamos por finalización de tarea de forma ascendente.
print(len(recursive_activity_selector(arr)))
