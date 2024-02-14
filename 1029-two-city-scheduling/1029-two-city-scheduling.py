class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        container = []
        for a,b in costs:
            container.append([b-a, a, b])
        container.sort()
        sol = 0
        for i in range(len(container)):
            if i < len(costs) //2:
                sol += container[i][2]
            else:
                sol += container[i][1]
        return sol
            
        