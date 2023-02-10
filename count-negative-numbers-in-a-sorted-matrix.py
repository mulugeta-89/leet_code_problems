class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for item in grid[i]:
                if item < 0:
                    count += 1
        return count