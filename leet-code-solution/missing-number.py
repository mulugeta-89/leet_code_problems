class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #nums.sort()
        #maxi = max(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return -1

        