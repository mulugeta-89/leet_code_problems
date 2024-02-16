class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles > 0 and target > 1:
            if(target % 2 != 0):
                count += 2
            else:
                count += 1
            target = target // 2
            maxDoubles -= 1
        count += (target-1)
        return count