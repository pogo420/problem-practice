# DP approach, show the brute force approach every were.

class Solution:
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
        length = 3
        max_length = 2
        start_index = 0
        while length <= len(s):
            start = 0
            while start < len(s) - length + 1:
                end = start + length - 1
                if s[end] == s[start] and db[start+1][end-1] == 1:
                    db[start][end] = 1
                    if length >= max_length:
                        max_length = length
                        start_index = start

                start += 1
            length += 1

        return s[start_index:start_index+max_length]


if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbd"))
