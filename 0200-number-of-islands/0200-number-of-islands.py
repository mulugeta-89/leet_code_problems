def explore(grid, r,c, visited):
    rowInbounds = r >= 0 and r < len(grid)
    colInbounds = c >= 0 and c < len(grid[0])
    if not rowInbounds or  not colInbounds or grid[r][c] == "0":
        return False
    position = str(r) + "," + str(c)
    if position in visited:
        return False
    visited.add(position)
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)
    return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if explore(grid, r, c, visited):
                    count += 1
        return count
        