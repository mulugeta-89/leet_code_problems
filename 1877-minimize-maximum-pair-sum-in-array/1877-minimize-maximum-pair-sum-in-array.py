class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi = -float("inf")
        left, right = 0, len(nums)-1
        while left < right:
            sumi = nums[left] + nums[right]
            maxi = max(maxi, sumi)
            left += 1
            right -= 1
        return maxi