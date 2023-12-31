class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxi = max(costs)
        storage = [0] * (maxi+1)
        sorted = []
        for i in costs:
            storage[i] += 1
        for ind, val in enumerate(storage):
            for i in range(val):
                sorted.append(ind)
        count = 0
        for i in range(len(sorted)):
            if coins < sorted[i]:
                break
            coins -= sorted[i]
            count += 1
        return count
        