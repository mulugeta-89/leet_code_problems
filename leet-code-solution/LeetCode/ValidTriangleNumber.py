class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                ind =  bisect_left(nums, nums[i]+nums[j], lo=j+1)-1
                count += ind-j
        return count