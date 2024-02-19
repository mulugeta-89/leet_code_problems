class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        sol = 0
        other_grid = [[0 for x in range(c)] for _ in range(r)]
        max_each_row = []
        max_each_column = []
        for item in grid:
            max_each_row.append(max(item))
        for i in range(c):
            maxi = -1
            for j in range(r):
                maxi = max(maxi, grid[j][i])
            max_each_column.append(maxi)
        for i in range(r):
            for j in range(r):
                other_grid[i][j] = min(max_each_row[i], max_each_column[j])
        for i in range(r):
            for j in range(r):
                sol += other_grid[i][j] - grid[i][j]
        return sol
        