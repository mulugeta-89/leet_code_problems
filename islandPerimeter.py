def perimeter(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                sum += 4
                if i > 0 and grid[i-1][j]:
                    sum -= 2
                if j > 0 and grid[i][j-1]:
                    sum -= 2
    return sum

print(perimeter([[1]]))