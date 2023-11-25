class Solution:
    def isFascinating(self, n: int) -> bool:
        digits = [i for i in range(1,10)]
        digits = map(lambda x: str(x), digits)
        digits = "".join(digits)
        new_n = str(n*2) + str(n) + str(n*3)
        if len(new_n) > len(digits):
            return False
        digits = set(digits)
        new_n = set(new_n)
        
        return True if digits.issubset(new_n) and "0" not in new_n else False
        
        
        