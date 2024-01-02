class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        container = []
        sol = []
        for item in points:
            x = item[0]
            y = item[1]
            dis = sqrt((abs(x-0)**2) + (abs(y-0)**2))
            container.append((item, dis))
        container.sort(key=lambda x: x[1])
        
        for i in range(k):
            sol.append(container[i][0])
        return sol
        