
def subset_sum_patterns(d, target: int, result: list, curr: list, pos):
    if target == 0:
        result.append(curr.copy())
        return

    for i in range(pos, len(d)):
        curr.append(d[i])
        subset_sum_patterns(d, target - d[i], result, curr, pos + 1)
        curr.pop()


def subset_sum_recur(d, target, asi):

    if target == 0:
        return True

    if asi == 0 and target > 0:
        return False

    if d[asi - 1] <= target:
        return subset_sum_recur(d, target - d[asi - 1], asi - 1) or subset_sum_recur(d, target, asi - 1)

    else:
        return subset_sum_recur(d, target, asi - 1)


if __name__ == '__main__':
    data = [2, 3, 7, 8, 10]
    t = 12
    r = []
    c = []
    subset_sum_patterns(data, t, r, c, 0)
    print(r)

    print(subset_sum_recur(data, t, len(data)))



