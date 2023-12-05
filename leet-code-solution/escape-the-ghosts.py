class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def findDistance(x,y):
            a,b = target
            # return abs(abs(x)-abs(a)) + abs(abs(y)-abs(b))
            return max(x,a) - min(x,a) + max(y,b) - min(y,b)
        me = findDistance(0,0)
        for a,b in ghosts:
            if findDistance(a,b) <= me:
                return False
        return True
        