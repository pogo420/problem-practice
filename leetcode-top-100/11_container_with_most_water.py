from typing import List


class Solution_brute_force:
    """O(n^2) Application"""
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(0, len(height)-1):
            for j in range(i+1, len(height)):
                temp_area = (j-i) * min(height[j], height[i])
                if max_area < temp_area:
                    max_area = temp_area
        return max_area


class Solution:
    """O(n) Application"""
    # moving the smaller one increase area.
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height)-1

        while l < r:
            temp = (r-l) * min(height[l], height[r])
            if max_area < temp:
                max_area = temp
            if height[l] < height[r]:  # move to next level
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([4, 3, 2, 1, 4]))
    print(Solution().maxArea([1, 2, 1]))
