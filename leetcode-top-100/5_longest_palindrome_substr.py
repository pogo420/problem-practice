# DP approach, show the brute force approach every were.
# all substr in O(n^2) complexity and checking palindrome O(n) for each substr.
# Total O(n^3) complexity


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


class Solution_jag:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        count = 2
        max_length = 0
        start = 0
        end = 0
        dp = [
            [0 for i in range(len(s))] for j in range(len(s))
        ]

        for i in range(length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                if count > max_length:
                    start = i
                    end = i+1
                    max_length = count
            else:
                dp[i][i + 1] = 0
            dp[i][i] = 0

        for gap in range(2, length):
            for i in range(length-gap):
                j = gap + i

                if (s[i] == s[j]) and (dp[i+1][j-1] == 1):
                    dp[i][j]=1
                    count = j-i+1
                    if count > max_length:
                        start = i
                        end = i + 1
                        max_length = count

        return s[start:end+1]


if __name__ == '__main__':
    # print(Solution().longestPalindrome("cbbp"))  # this use case is failing
    print(Solution().longestPalindrome("aaaabbaa"))
