

def balanced_parenthesis(n, pattern: list, open_, close_, pos):
    if open_ == 0 and close_ == 0:
        # base or termination , when both open and close is exhausted
        print(pattern)
        return

    if open_ > 0:   # start is always feasible as long as we have available, open is in beginning
        # as every pattern should start with open.
        # print(pattern)
        pattern[pos] = "{"
        balanced_parenthesis(n, pattern, open_-1, close_, pos+1)

    if close_ > open_:  # choice of close is only available when close is more available
        pattern[pos] = "}"
        balanced_parenthesis(n, pattern, open_, close_-1, pos+1)


if __name__ == '__main__':
    n = 3
    d = [""] * 2 * n  # 2 n boxes to pattern; n open and n close
    balanced_parenthesis(n, d, n, n, 0)


# check the recursion tree
