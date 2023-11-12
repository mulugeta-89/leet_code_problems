class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maximum = -1
        start = 0
        end = 1
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                sums = sum(nums[start:end])
                maximum = max(maximum, sums)
                start = end
                end = start + 1

            else:
                end += 1
            if end == len(nums):
                sums = sum(nums[start:end])
                maximum = max(maximum, sums)
        return maximum
        