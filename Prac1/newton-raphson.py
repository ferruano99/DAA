def f(x):
    return x ** 2 - a

def fp(x):
    return 2 * x

def newton_raphson(x, previo):
    if abs(f(x)) < 10**-6:
        print("{:.4f}".format(abs(x)))
    else:
        newton_raphson(previo - (f(previo) / fp(previo)), x)

if __name__ == '__main__':
    a = int(input())
    newton_raphson(a, a)