class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            correct = nums[i]-1
            if correct < n:
                if nums[i] >= 1 and nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    i += 1
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return nums[-1]+1
        