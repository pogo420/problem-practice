
def isPalindrome(s: str, l, r):
    if l > r:  # base case 1 for even length
        return True
    if l == r:  # base case 2 for odd length
        return True

    if s[l] != s[r]:
        return False

    return isPalindrome(s, l + 1, r - 1)


def powersubsets(s: str, i: int, curr_s: str, result_set: list):
    # check notes
    if i == len(s):  # base case when we are hitting the end of string
        result_set.append(curr_s)
        return
    powersubsets(s, i + 1, curr_s, result_set)  # don't include
    powersubsets(s, i + 1, curr_s + s[i], result_set)  # include


if __name__ == '__main__':
    # print(isPalindrome("aba", 0, 2))
    array = []
    powersubsets("abc", 0, "", array)
    print(array)
