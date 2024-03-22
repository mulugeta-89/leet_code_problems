class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        sol = float("inf")

        def canHeat(radius):
            l, r = 0, 0
            while l < len(houses) and r < len(heaters):
                if abs(houses[l]-heaters[r]) <= radius:
                    l += 1
                else:
                    r += 1
            return l == len(houses)
        l, r = 0, max(houses[-1], heaters[-1])

        while l <= r:
            mid = (l+r)//2
            if canHeat(mid):
                sol = min(sol, mid)
                r = mid-1
            else:
                l = mid+1
        return sol