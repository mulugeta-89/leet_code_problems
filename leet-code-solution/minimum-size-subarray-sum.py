class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        sol = float("inf")
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                sol = min(sol, right-left+1)
                curr_sum -= nums[left]
                left += 1
        return sol if sol != float("inf") else 0
        