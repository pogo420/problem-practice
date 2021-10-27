
def cc(coins, target, l):

    if target == 0:
        return 1  # empty coin

    if l == 0 and target > 0:
        return 0  # no ways

    if coins[l -1] <= target:
        return cc(coins, target - coins[l -1], l) + cc(coins, target, l - 1)

    else:
        return cc(coins, target, l - 1)


if __name__ == '__main__':
    c = [1, 2, 3]
    t = 5
    print(cc(c, t, 3))
