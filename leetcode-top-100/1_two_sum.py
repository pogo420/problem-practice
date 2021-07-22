from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track_dict = {}
        count = 0
        for num in nums:
            if track_dict.get(target-num):  # checking for complement
                return [track_dict.get(target-num), count]
            track_dict[num] = count
            count += 1
