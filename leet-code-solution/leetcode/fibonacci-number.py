def founder(n,dicti):
    if n in dicti:
        return dicti[n]
    if n == 1 or n == 0:
        return n
    dicti[n] = founder(n-1, dicti) + founder(n-2, dicti)
    return dicti[n]
class Solution:
    def fib(self, n: int) -> int:
        dicti = {}
        return founder(n, dicti)
        