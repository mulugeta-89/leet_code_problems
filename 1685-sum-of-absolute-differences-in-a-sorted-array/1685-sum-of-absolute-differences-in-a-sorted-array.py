import numpy as np
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sol_arr = []
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        for i in range(len(nums)):
            left_sum = prefix_sum[i] -nums[i]
            right_sum = prefix_sum[-1] - prefix_sum[i]

            left_count = i
            right_count = len(nums)-1-i

            left_count_sum =(left_count*nums[i]) - left_sum
            right_count_sum = right_sum-right_count*nums[i]
            sol_arr.append(left_count_sum + right_count_sum)
        return sol_arr
