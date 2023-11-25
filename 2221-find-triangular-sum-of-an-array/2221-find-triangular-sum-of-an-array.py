class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        new_arr = []
        while len(nums)!= 1:
            for i in range(1, len(nums)):
                run = (nums[i]+nums[i-1])%10
                new_arr.append(run)
            nums = new_arr
            new_arr = []
        return nums[0]
        