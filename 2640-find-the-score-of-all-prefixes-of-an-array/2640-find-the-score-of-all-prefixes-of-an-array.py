class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maximum = nums[0]
        prefix_sum = []
        prefix_sum.append(2*nums[0])
        for i in range(1, len(nums)):
            maximum  = max(maximum, nums[i])
            prefix_sum.append(prefix_sum[i-1] + nums[i] + maximum)
        return prefix_sum
        