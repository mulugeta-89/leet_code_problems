class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        merged = []
        count = 0
        for interval in points:
            if merged and merged[-1][-1] >= interval[0]:
                merged[-1][-1] = min(merged[-1][-1], interval[1])
                count += 1
            else:
                merged.append(interval)
        return len(merged)
        