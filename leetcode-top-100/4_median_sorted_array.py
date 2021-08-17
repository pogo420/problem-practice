from typing import List


class Solution:

    def findMedianSortedArrays_naive(self, nums1: List[int], nums2: List[int]) -> float:
        # Time: O(n+m) solution Space: O(1)

        if (len(nums1) + len(nums2)) % 2 == 0:
            median_index1 = (len(nums1) + len(nums2)) / 2
            median_index2 = median_index1 - 1
        else:
            median_index1 = ((len(nums1) + len(nums2)) - 1) / 2
            median_index2 = median_index1

        median_val = 0
        l = r = 0
        count = 0
        val = 0
        hit_index = 0
        while count < len(nums1)+len(nums2):

            if hit_index >= 2:  # for even cases, optimization to reduce iteration
                break

            if hit_index >= 1 and median_index1 == median_index2:  # for odd cases, optimization to reduce iteration
                break

            if l >= (len(nums1) - 1):  # to prevent array out of bound
                l = len(nums1) - 1

            if r >= (len(nums2) - 1):  # to prevent array out of bound
                r = len(nums2)-1

            if nums1[l] < nums2[r]:
                val = nums1[l]

                if count == median_index1 or count == median_index2:  # matching index
                    median_val += val
                    hit_index += 1
                l += 1

            else:
                val = nums2[r]

                if count == median_index1 or count == median_index2:  # matching index
                    median_val += val
                    hit_index += 1
                r += 1

            count += 1

        if median_index1 == median_index2:
            return median_val  # for odd cases
        return median_val/2 # for even cases


if __name__ == '__main__':

    a = [1, 3]
    b = [2, 9, 10]
    print(Solution().findMedianSortedArrays_naive(a, b))
