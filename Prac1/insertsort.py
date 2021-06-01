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


def insert_sort(i, a, x):
    a.insert(i, x)
    sort(a, i)


if __name__ == '__main__':
    length = int(input())
    l = [int(i) for i in input().split()]
    to_insert = int(input())
    insert_sort(length, l, to_insert)
