# DP approach, show the brute force approach every were.
# all substr in O(n^2) complexity and checking palindrome O(n) for each substr.
# Total O(n^3) complexity


class Solution_dp:
    def longestPalindrome(self, s: str) -> str:
        # less than 2 cases
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        db = [
            [0 for i in range(len(s))] for j in range(len(s))
        ]

        for i in range(len(s)):
            db[i][i] = 1  # filling the diagonal elements
            if s[i] == s[min(i+1, len(s)-1)]:  # next to diagonal
                db[i][min(i+1, len(s)-1)] = 1

        # generating remaining elements
        length = 2
        max_length = -1
        start_index = 0
        while length <= len(s):
            start = 0
            while start < len(s) - length + 1:
                end = start + length - 1
                if (s[end] == s[start]) and (db[start+1][end-1] == 1):
                    db[start][end] = 1
                    if length >= max_length:
                        max_length = length
                        start_index = start
                print(start, length, max_length, s[start], s[end], db[start+1][end-1])
                start += 1
            length += 1
        return s[start_index:start_index+max_length]


## mirror technique, Expland around the center
class Solution:

    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_length = 0

        for i in range(len(s)):
            # odd cases
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_length:
                    res = s[l:r+1]
                    res_length = r-l+1
                l -= 1
                r += 1

            # even cases
            l = i
            r = i +1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res_length:
                    res = s[l:r+1]
                    res_length = r-l+1
                l -= 1
                r += 1
        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbp"))  # this use case is failing
    print(Solution().longestPalindrome("aaaabbaa"))
    print(Solution().longestPalindrome("aabbaaabcdefedcba"))
