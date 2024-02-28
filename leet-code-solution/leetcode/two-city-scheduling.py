class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        sol = 0
        costs.sort(key=lambda x : (x[0]- x[1]))
        for i in range(len(costs)):
            a,b = costs[i]
            if i < n //2:
                sol += a
            else:
                sol += b
        return sol

        