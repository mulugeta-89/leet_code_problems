class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        k = len(matrix[0])
        sol_arr = []
        for i in range(k):
            temp = []
            for item in matrix:
                temp.append(item[i])
            sol_arr.append(temp)
        return sol_arr
        