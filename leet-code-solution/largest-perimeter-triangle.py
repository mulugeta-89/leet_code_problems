class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                maxi = max(nums[i] + nums[i+1] + nums[i+2], maxi)
        return maxi
        