from math import comb


def pascal_triangle(n):
    if n < 1:
        return
    print([1])
    for i in range(0, n - 1):
        row = [1]
        for j in range(1, i + 2):
            row.append(comb(i + 1, j))
        print(row)


pascal_triangle(5)
