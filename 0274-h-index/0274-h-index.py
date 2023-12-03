class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort(reverse=True)
        if len(c)== 1 and c[0] >= 1:
            return 1
        if c[-1] >= len(c):
            return len(c)
        for i in range(len(c)):
            if c[i] < i+1:
                return i
        return 0
            