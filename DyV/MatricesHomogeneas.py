def eshomogenea(m, inifila, finfila, inicol, fincol):
    n = m[inifila][inicol]
    for i in range(inifila, finfila + 1):
        for j in range(inicol, fincol + 1):
            if m[i][j] != n:
                return False
    return True


def dyv(m, inifila, finfila, inicol, fincol):
    if inifila == finfila and inicol == fincol:
        return 1
    elif eshomogenea(m, inifila, finfila, inicol, fincol):
        return 1
    else:
        mitadfila = (inifila + finfila) // 2
        mitadcol = (inicol + fincol) // 2
        if inifila < finfila:
            if inicol < fincol:
                v1 = dyv(m, inifila, mitadfila, inicol, mitadcol)
                v2 = dyv(m, inifila, mitadfila, mitadcol + 1, fincol)
                v3 = dyv(m, mitadfila + 1, finfila, inicol, mitadcol)
                v4 = dyv(m, mitadfila + 1, finfila, mitadcol + 1, fincol)
                return v1 + v2 + v3 + v4
            else:
                v2 = dyv(m, inifila, mitadfila, inicol, fincol)
                v3 = dyv(m, mitadfila + 1, finfila, inicol, fincol)
                return v2 + v3
        else:
            v1 = dyv(m, inifila, finfila, inicol, mitadcol)
            v2 = dyv(m, inifila, finfila, mitadcol + 1, fincol)
            return v1 + v2


m = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
print(dyv(m, 0, len(m) - 1, 0, len(m[0]) - 1))
