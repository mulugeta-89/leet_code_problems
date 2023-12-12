class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 0:
            return 0
        maxi = 1
        counter = 1
        for i in range(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                counter += 1
                maxi = max(maxi, counter)
            else:
                maxi = max(maxi, counter)
                counter = 1
        return maxi