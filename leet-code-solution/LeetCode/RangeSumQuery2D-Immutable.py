class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])
        prefix_sum = [[0 for i in range(columns)] for j in range(rows)]
        prefix_sum[0][0] = matrix[0][0]
        for i in range(1,columns):
            prefix_sum[0][i] = prefix_sum[0][i-1] + matrix[0][i]
        for i in range(1, rows):
            prefix_sum[i][0] = prefix_sum[i-1][0] + matrix[i][0]
        for r in range(1,rows):
            for c in range(1,columns):
                prefix_sum[r][c] = prefix_sum[r][c-1] + prefix_sum[r-1][c] - prefix_sum[r-1][c-1] + matrix[r][c]
        self.prefix_sum = prefix_sum
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sol = self.prefix_sum[row2][col2] - (self.prefix_sum[row2][col1-1] if col1 > 0 else 0) - (self.prefix_sum[row1-1][col2] if row1 > 0 else 0) + (self.prefix_sum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0)
        return sol


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)