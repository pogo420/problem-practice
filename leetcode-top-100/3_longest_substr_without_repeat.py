from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        busket: Dict = {}
        count = 0
        start = 0
        lstr = 0

        for char in s:
            if char in busket:
                start = max(start, busket.get(char) + 1)
            busket[char] = count
            lstr = max(lstr, count-start+1)
            count += 1
        return lstr


if __name__ == '__main__':
    print(
        Solution().lengthOfLongestSubstring("abcabcdeabcbc"),
        Solution().lengthOfLongestSubstring("abcabcbb"),
        Solution().lengthOfLongestSubstring("pwwkew"),
    Solution().lengthOfLongestSubstring("abba")
    )
