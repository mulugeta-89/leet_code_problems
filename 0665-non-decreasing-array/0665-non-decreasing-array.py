class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        check = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if check:
                    return False
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                check = True
        return True
        