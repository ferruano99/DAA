import sys


def ej1(v, i, f, m):  # MAL
    if i == f:
        return v[i], 1, False, False
    else:
        mitad = (i + f) // 2
        v1, acc1, rep1, mayoritario1 = ej1(v, i, mitad, m)
        v2, acc2, rep2, mayoritario2 = ej1(v, mitad + 1, f, m)
        if v1 == v2:
            nuevoacc = acc1 + acc2
            if nuevoacc > m:
                return v1, nuevoacc, True, True
            else:
                return v1, nuevoacc, True, False
        else:
            if rep1:
                if acc1 > acc2:
                    return v1, acc1, rep1, mayoritario1
                else:
                    return v2, acc2, rep2, mayoritario2
            else:
                return v2, acc2, rep2, mayoritario2


def factible(m, nuevax, nuevay, s_acc, s_opt):
    if nuevax < 0 or nuevax >= len(m):
        return False
    if nuevay < 0 or nuevay >= len(m[0]):
        return False
    if m[nuevax][nuevay] == "X" or m[nuevax][nuevay] == "M":
        return False
    if s_acc > s_opt:
        return False
    return True


def ej2(m, etapax, etapay, s_acc, s_opt, movx, movy):
    intento = 0
    while intento < len(movx):
        nuevax = etapax + movx[intento]
        nuevay = etapay + movy[intento]
        if factible(m, nuevax, nuevay, s_acc, s_opt):
            m[nuevax][nuevay] = "X"
            s_acc[0] += 1
            if nuevax == len(m) - 1 and nuevay == len(m[0]) - 1:
                if s_acc[0] < s_opt[0]:
                    s_opt[0] = s_acc[0]
                # m[nuevax][nuevay] = "S"
            else:
                ej2(m, nuevax, nuevay, s_acc, s_opt, movx, movy)
            m[etapax][etapay] = " "
            s_acc[0] -= 1
        intento += 1


m = [
     ["E", " ", " ", " ", " ", " ", " ", "M", "M", "M"],
     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", "M", "M", "M", "M", "M", " ", " "],
     [" ", " ", " ", "M", "M", "M", " ", " ", " ", " "],
     [" ", " ", " ", "M", "M", "M", " ", " ", " ", " "],
     [" ", " ", " ", "M", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", "M", "M", "M", "M", " ", " ", " "],
     [" ", " ", " ", "M", " ", " ", "M", " ", " ", " "],
     [" ", " ", " ", "M", " ", " ", "M", " ", " ", " "],
     [" ", " ", " ", "M", " ", " ", "M", "M", "M", "S"]
]

movx = [1, 0, -1, 0]
movy = [0, 1, 0, -1]
s_opt = [sys.maxsize]
ej2(m, 0, 0, [0], s_opt, movx, movy)
print(s_opt)
