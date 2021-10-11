

def search_2d(array, key: int) -> tuple:
    i = 0
    j = len(array[i]) - 1

    while len(array) > i >= 0 and 0 <= j < len(array[i]):
        if array[i][j] == key:
            return i, j
        if array[i][j] > key:  # move towards less
            j -= 1
        else:
            i += 1

    return -1, -1


if __name__ == '__main__':
    a = [
            [10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50]
    ]

    (i, j) = search_2d(a, 29)
    print(i, j)
