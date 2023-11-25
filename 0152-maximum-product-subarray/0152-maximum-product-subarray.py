class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = -float("inf")
        maxi2 = -float("inf")
        prod = 1
        for i in nums:
            prod *= i
            if prod > maxi:
                maxi = prod
            if prod == 0:
                prod = 1
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            if prod > maxi2:
                maxi2 = prod
            if prod == 0:
                prod = 1
        return max(maxi, maxi2)