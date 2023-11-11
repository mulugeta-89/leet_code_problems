class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
    
        for item in image:
            small = []
            other = item[::-1]
            for i in other:
                if i == 1:
                    i = 0
                else:
                    i = 1
                small.append(i)
            res.append(small)
        return res
        