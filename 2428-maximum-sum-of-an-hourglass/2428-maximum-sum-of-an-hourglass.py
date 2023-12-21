class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxi = 0
        for j in range(0, len(grid)-2):
            for i in range(2, len(grid[0])):
                temp = grid[j][i-2] + grid[j][i-1] + grid[j][i]
                temp += grid[j+1][i-1]
                temp += grid[j+2][i-2] + grid[j+2][i-1] + grid[j+2][i]
                maxi = max(maxi, temp)
        return maxi
        