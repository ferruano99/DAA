def feasable(subset, candidate):  # Condición para obtener el candidato
    if candidate % min(subset) != 0:
        return False
    return True


def subsets_wrapper(set, m):
    solution = []
    for p_candidate in range(len(set)):
        subset = [set[p_candidate]]
        subsets(set, m, set[p_candidate], subset, p_candidate, solution)
    print(len(solution))


def subsets(set, m, candidate, subset, p_candidate, total_subsets):
    if len(subset) == m:  # Condición para obtener una solución
        total_subsets.append(subset)
    else:
        for i in range(p_candidate + 1, len(set)):  # Algoritmo de backtracking
            if feasable(subset, set[i]):
                subset.append(set[i])
                subsets(set, m, candidate + 1, subset, i, total_subsets)
                del subset[-1]


n = int(input())
set = [int(i) for i in input().split()]
m = int(input())
set.sort()
subsets_wrapper(set, m)
