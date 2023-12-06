class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol_arr = []
        while matrix:
            sol_arr += matrix.pop(0)
            if matrix and matrix[0]:
                for item in matrix:
                    sol_arr.append(item.pop())
            if matrix and matrix[0]:
                sol_arr += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for item in matrix[::-1]:
                    sol_arr.append(item.pop(0))
        return sol_arr