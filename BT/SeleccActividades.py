def factible(etapa, c, f, sol):
    for i in range(etapa):
        if c[etapa] < f[i] and sol[i] == 0:
            return False
    return True

def planificacion_tareas(c, f, n, etapa, sol):
    exito = False
    intento = 0
    while intento < 2 and not exito:
        if factible(etapa, c, f, sol) or intento == 1:
            sol[etapa] = intento
            if etapa == n - 1:
                exito = True
            else:
                exito = planificacion_tareas(c, f, n, etapa + 1, sol)
                if not exito:
                    sol[etapa] = 1
        intento += 1
    return exito


n = 11
ini = [1, 2, 0, 5, 8, 5, 6, 8, 3, 3, 12]
fin = [4, 13, 6, 7, 12, 9, 10, 11, 8, 5, 14]
sol = [1] * n

exit = planificacion_tareas(ini, fin, n, 0, sol)
if exit:
    print(sol)
else:
    print("nada")
