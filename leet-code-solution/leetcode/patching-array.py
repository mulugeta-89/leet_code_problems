class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        k = len(nums)
        count = 0
        reach = 0
        i = 0
        while reach < n:
            if i < k and nums[i] <= reach+1:
                reach += nums[i]
                i += 1
            elif i >= k:
                reach += reach+1
                count += 1
            else:
                reach += reach+1
                count += 1
        return count
        