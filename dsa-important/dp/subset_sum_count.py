

def count_subset_sum(a, target):
    d = [[-1 for _ in range(target+1)] for _ in range(len(a)+1)]

    # initialization
    for el in range(len(a)+1):
        for ta in range(target+1):
            if ta == 0:
                d[el][ta] = 1
            elif el == 0 and ta > 0:
                d[el][ta] = 0

    # logic
    for el in range(1, len(a)+1):
        for ta in range(1, target+1):
            if a[el- 1] <= ta:
                d[el][ta] = d[el-1][ta - a[el - 1]] + d[el -1][ta]
            else:
                d[el][ta] = d[el - 1][ta]

    return d[-1][-1]


if __name__ == '__main__':
    a = [1, 2, 3, 3]
    t = 6
    print(count_subset_sum(a, t))
