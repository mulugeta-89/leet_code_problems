class Solution:
    def check(self, nums: List[int]) -> bool:
        a = sorted(nums)
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == a:
                return True
        return False
        