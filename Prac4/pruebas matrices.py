m = [[0 for i in range(5)] for j in range(4)]  # matriz de 4x5
m1 = [[0 for i in range(len(m[0]))] for j in range(3)]  # 3 x 5


def p_m(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print()


print(m1)
print()
p_m(m1)  # 4 filas 5 columas
