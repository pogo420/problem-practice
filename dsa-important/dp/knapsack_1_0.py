
d = [[-1 for i in range(100)] for j in range(100)]


def knapsack_1_0_recur(val: list, weight: list, max_weight: int, result: list, current: list, pos: int) -> list:

    if pos == len(val):
        result.append(current.copy())
        return result

    if sum(current) + val[pos] < max_weight:
        current.append(val[pos])
        knapsack_1_0_recur(val, weight, max_weight, result, current, pos+1)

        current.pop()
        knapsack_1_0_recur(val, weight, max_weight, result, current, pos + 1)
    else:
        knapsack_1_0_recur(val, weight, max_weight, result, current, pos + 1)


def knapsack_1_0_recur_(val: list, weight: list, max_weight: int, array_length: int) -> int:

    if array_length == 0 or max_weight == 0:
        return 0

    if weight[array_length - 1] <= max_weight:
        return max(
            val[array_length-1]
            + knapsack_1_0_recur_(val, weight, max_weight - weight[array_length - 1], array_length - 1),
            knapsack_1_0_recur_(val, weight, max_weight, array_length - 1)
        )
    else:
        return knapsack_1_0_recur_(val, weight, max_weight, array_length - 1)


def knapsack_1_0_memorize(val: list, weight: list, max_weight: int, array_length: int) -> int:

    if array_length == 0 or max_weight == 0:
        return 0

    if d[max_weight][array_length] != -1:
        return d[max_weight][array_length]

    if weight[array_length - 1] <= max_weight:
        d[max_weight][array_length] = max(
            val[array_length-1]
            + knapsack_1_0_recur_(val, weight, max_weight - weight[array_length - 1], array_length - 1),
            knapsack_1_0_recur_(val, weight, max_weight, array_length - 1)
        )
        return d[max_weight][array_length]
    else:
        d[max_weight][array_length] = knapsack_1_0_recur_(val, weight, max_weight, array_length - 1)
        return d[max_weight][array_length]


if __name__ == '__main__':
    val_ = [1, 4, 8, 7]
    r = []
    knapsack_1_0_recur(val_, [], 9, r, [], 0)
    print(r)

    val_ = [1, 4, 8, 7]
    wei = [1, 4, 8, 7]
    val = knapsack_1_0_recur_(val_, wei, 10, len(val_))
    print(val)

    val_ = [1, 4, 8, 7]
    wei = [1, 4, 8, 7]
    val = knapsack_1_0_memorize(val_, wei, 10, len(val_))
    print(val)
