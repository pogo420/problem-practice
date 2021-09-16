from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> list:
        complement = {}
        count = 0
        result = []
        for i in nums:
            if target-i in complement:
                # print(target, i, complement)
                result.append([complement.get(target-i), i])
            complement[i] = nums[count]
            count += 1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        actual_target = 0
        duplicate_set = set()
        for i in range(len(nums)):
            temp_target = actual_target - nums[i]
            sum_2s: List = Solution.twoSum(nums[i+1:], temp_target)
            for sum_2 in sum_2s:
                result_ = [nums[i]] + sum_2
                sorted_result = tuple(sorted(result_))
                # print(sorted_result, duplicate_set)
                if sorted_result in duplicate_set:
                    continue
                result.append(result_)
                duplicate_set.add(sorted_result)

        return result


if __name__ == '__main__':
    # print(Solution.twoSum([0, 1, 2, -1, -4], 1))
    # print(Solution.twoSum([1, 2, -1, -4], 0))
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # print(Solution().threeSum([0]))
