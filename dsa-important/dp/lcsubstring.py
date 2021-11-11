def lcs(s1, s2, m, n, count):

    if m == 0 or n == 0:
        return count

    if s1[m - 1] == s2[n - 1]:
        count = lcs(s1, s2, m - 1, n - 1, count + 1)

    else:
        count = max(count,
                    max(
                        lcs(s1, s2, m - 1, n, 0),
                        lcs(s1, s2, m, n - 1, 0)
                    )
                    )
    return count


if __name__ == '__main__':
    a = "abcdgfh"
    b = "abedgfhr"
    print(lcs(a, b, len(a), len(b), 0)
          )
