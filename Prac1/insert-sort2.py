def sort(a, i):
    if i == 0 and len(a) <= 1:
        print(a[0])
    elif i == 0 and len(a) > 1:
        for i in a:
            print(i, end=' ')
    else:
        b = list(a)
        m = min(a)
        b.remove(m)
        print(m, end=' ')
        sort(b, i - 1)


def insert_sort_recursivo(i, a):
    sort(a, i - 1)


if __name__ == '__main__':
    length = int(input())
    l = [int(i) for i in input().split()]
    insert_sort_recursivo(length, l)
