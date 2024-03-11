
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length = 2**(n-1)
        mid = length // 2
        if k <= mid:
            return self.kthGrammar(n-1,k)
        else:
            return int(not(self.kthGrammar(n-1, k-mid)))
        
        