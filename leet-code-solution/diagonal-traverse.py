class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dicti = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dicti[i+j].append(mat[i][j])
        result = []
        for k in sorted(dicti.keys()):
            if k % 2 == 0:
                dicti[k].reverse()
            result += dicti[k]
        return result
        