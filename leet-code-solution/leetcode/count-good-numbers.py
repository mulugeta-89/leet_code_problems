class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens = n // 2 if n % 2 == 0 else (n//2) + 1
        odds = n // 2
        def power(x,y,m):
            if y == 0:
                return 1
            if y == 1:
                return x % m
            if y % 2 == 0:
                return power((x*x)%m, y//2, m)
            else:
                return (x*power((x*x)%m, y // 2, m)) % m
        return (power(5, evens, ((10 ** 9) + 7)) * power(4, odds, ((10 ** 9) + 7))) % ((10 ** 9) + 7)
        