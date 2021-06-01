# a = 12346 x = 5 --> sol = 123456

def rec(a, x):
    if x >= a % 10:
        return x + a * 10
    else:
        return a % 10 + 10 * rec(a // 10, x)


print(rec(234, 1))
