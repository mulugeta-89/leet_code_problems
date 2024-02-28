class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = n
        if n < 0:
            n = -1 * n
        
        def finder(x,n):
            if n == 0:
                return 1
            if n%2 == 0:
                half = finder(x, n//2)
                return half * half
            else:
                half = finder(x, (n-1)//2)
                return x * half * half
        a = finder(x,n)
        if p < 0:
            return 1/a
        return a
        