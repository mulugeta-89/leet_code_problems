class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ternary = ""
        while n > 0:
            ternary += str(n%3)
            n //= 3
        return False if "2" in ternary else True
        