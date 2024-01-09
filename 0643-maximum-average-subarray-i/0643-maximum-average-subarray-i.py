class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        first = sum(nums[:k])
        maxi = max(-float("inf"), first)
        while r < len(nums):
            first += nums[r]
            first -= nums[l]
            maxi = max(maxi, first)
            l += 1
            r += 1
        return maxi/k