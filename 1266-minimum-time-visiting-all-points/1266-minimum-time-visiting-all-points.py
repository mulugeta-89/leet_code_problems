class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            x, y = points[i]
            target_x, target_y = points[i + 1]
            ans += max(abs(target_x - x), abs(target_y - y))

        return ans