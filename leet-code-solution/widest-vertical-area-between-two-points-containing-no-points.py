class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        sol = -1
        for i in range(1, len(points)):
            sol = max(sol, points[i][0]-points[i-1][0])
        return sol
        