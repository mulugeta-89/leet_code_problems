class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        sol = float("inf")
        def canShip(cap):
            ships, currentCapacity = 1, cap
            for w in weights:
                if currentCapacity - w < 0:
                    ships += 1
                    currentCapacity = cap
                currentCapacity -= w
            return ships <= days
        while l <= r:
            mid = (l+r)//2
            if canShip(mid):
                sol = min(sol, mid)
                r = mid -1
            else:
                l = mid+1
        return sol
        