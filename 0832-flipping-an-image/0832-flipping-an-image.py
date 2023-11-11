class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for item in image:
            other = item[::-1]
            for i in range(len(other)):
                if other[i] == 1:
                    other[i] = 0
                else:
                    other[i] = 1
            res.append(other)
        return res
        