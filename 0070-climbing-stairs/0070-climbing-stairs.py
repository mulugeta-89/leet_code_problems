class Solution:
    def climbStairs(self, n: int) -> int:
        previous = 1
        next = 2
        total = 0
        if n == 1 or n ==2:
            return n
        for i in range(n-2):
            total = previous + next
            previous = next
            next = total
        return total
        