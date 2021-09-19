# How to do recursion?
# Base case
# Sub-problem <> problem relation
# generalize the relation.
# Recursion is always top down approach
# Recursive leap of faith


def basic(n: int, arr: list) -> list:
    if n == 0:  # base condition
        return arr
    arr.append(n)
    return basic(n-1, arr)  # return in each stage, for getting data in the end


def exp_1(a, b, i):
    if i > b:  # base case
        return 1
    return a * exp_1(a, b, i+1)  # generalized formulae


def exp_2(a, b):
    if b == 0:  # base case
        return 1
    return a * exp_2(a, b-1)  # a^n = a * a^(n-1)


if __name__ == '__main__':
    # print(basic(5, []))
    print(exp_1(2, 10, 1))
    print(exp_2(2, 10))
