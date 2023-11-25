class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, total = 0, 0, 0
        sol = -float("inf")
        while r < len(nums):
            total += nums[r]
            while (nums[r]*(r-l+1)) > total+k:
                total -= nums[l]
                l += 1
            sol = max(sol, (r-l)+1)
            r += 1
        return sol