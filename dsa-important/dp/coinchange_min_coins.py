
def cc_m(coins, target, l):

    if target == 0 or l == 0:
        return 0  # no min coin

    if coins[l -1] <= target:  # add one coin
        return 1 + min(cc_m(coins, target - coins[l -1], l), cc_m(coins, target, l - 1))

    else:
        return cc_m(coins, target, l - 1)


if __name__ == '__main__':
    c = [1, 2, 3]
    t = 5
    print(cc_m(c, t, 3))
