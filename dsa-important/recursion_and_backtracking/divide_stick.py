
def div_stick(n, result: list, curr_pattern: list):
    if n == 0:
        result.append(curr_pattern.copy())  # to prevent update of reference
        return

    for i in range(1, n+1):
        curr_pattern.append(i)
        div_stick(n-i, result, curr_pattern)
        curr_pattern.pop()  # undo changes as we move up


if __name__ == '__main__':
    r = []
    c = []
    div_stick(5, r, c)
    print(r)
