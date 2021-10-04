# ab = ab , aB, Ab, AB


def permutation_case_change(s: str, result: list, curr_str: str, pos):
    if pos == len(s):
        result.append(curr_str)
        return

    permutation_case_change(s, result, curr_str + s[pos].upper(), pos + 1)
    permutation_case_change(s, result, curr_str + s[pos].lower(), pos + 1)


if __name__ == '__main__':
    r = []
    s = "ab"
    permutation_case_change(s, r, "", 0)
    print(r)
