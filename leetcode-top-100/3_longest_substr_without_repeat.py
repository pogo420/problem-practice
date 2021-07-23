from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        busket: Dict = {}
        count = 0
        start = 0
        lstr = float("-inf")
        for char in s:
            if char in busket:
                start = count
                count += 1
                continue
            busket[char] = count
            lstr = max(count-start, lstr)
            count += 1
        return lstr


# a b c a b c d e a b c
