

def permutation(s: str, result: list, curr: str, pos: int):
    if pos == len(s):
        result.append(curr)
        return

    if s[pos].isdigit():
        permutation(s, result, curr + s[pos], pos + 1)  # ignore if digit
    else:
        permutation(s, result, curr + s[pos].upper(), pos + 1)
        permutation(s, result, curr + s[pos].lower(), pos + 1)


if __name__ == '__main__':
    s = "a1B2"
    r = []
    permutation(s, r, "", 0)
    print(r)
