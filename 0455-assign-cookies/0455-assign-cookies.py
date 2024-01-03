class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        first, second = 0,0
        g.sort()
        s.sort()
        count = 0
        while first < len(g) and second < len(s):
            if s[second] >= g[first]:
                count += 1
                first += 1
                second += 1
            else:
                second += 1
        return count
        