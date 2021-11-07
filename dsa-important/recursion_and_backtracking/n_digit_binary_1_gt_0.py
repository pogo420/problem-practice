

def get_digits(n: int, zeros: int, ones: int, pos: int, result: list, current: list):
    if n == 0:
        result.append(current.copy())
        return

    if n > 0:  # one always in the beginning
        current[pos] = 1
        get_digits(n-1, zeros, ones+1, pos+1, result, current)

    if ones > zeros:  # zero always one > zero
        current[pos] = 0
        get_digits(n - 1, zeros + 1, ones, pos + 1, result, current)


def binary_digits(N, curr, result, ones, zeros, pos):

    if zeros + ones == N:
        result.append(curr.copy())
        return

    if zeros + ones < N:
        curr[pos] = 1
        binary_digits(N, curr, result, ones + 1, zeros, pos + 1)

    if ones > zeros:
        curr[pos] = 0
        binary_digits(N, curr, result, ones, zeros + 1, pos + 1)


if __name__ == '__main__':
    n = 3
    r = []
    c = [0] * n
    get_digits(n, 0, 0, 0, r, c)
    print(r)

    n = 3
    r = []
    c = [0] * n
    binary_digits(n, c, r, 0, 0, 0)
    print(r)
