class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        sol = float("inf")

        def check(divisor):
            sumi = 0
            for num in nums:
                sumi += math.ceil(num/divisor)
            return sumi <= threshold
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                sol = min(sol, mid)
                r = mid - 1
            else:
                l = mid + 1
        return sol
        