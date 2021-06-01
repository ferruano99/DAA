def is_sorted(a):
    n = len(a)
    if n == 1:
        return True
    else:
        return (is_sorted(a[0: n // 2])) and (a[n // 2 - 1] <= a[n // 2] and is_sorted(a[n // 2: n]))


def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    else:
        p_m = a[: n // 2]
        s_m = a[n // 2:]
        merge_sort(p_m)
        merge_sort(s_m)
        return merge(p_m, s_m)


def merge(a, b):
    if a == []:
        return b
    elif b == []:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])


if __name__ == '__main__':
    print(is_sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(merge_sort([13, 31, 2, 4]))

    out = ([0] * 3)
    lista = [3, 2, 1, 4]
    out.extend(lista)
    print(out)
