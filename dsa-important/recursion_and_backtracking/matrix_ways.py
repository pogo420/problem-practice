# m*n matrix, ways to reach (right and bottom movement only). Left most to bottom right most.


def matrix(m, n):
    if m == 1 or n == 1:  # single row/column; base case
        return 1

    return matrix(m - 1, n) + matrix(m, n - 1)  # sub-problem division


if __name__ == '__main__':
    print(matrix(4, 3))
