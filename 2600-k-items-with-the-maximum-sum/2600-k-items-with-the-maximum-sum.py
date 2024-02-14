class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes > k:
            return k
        remainder = k-numOnes-numZeros
        if remainder <= 0:
            return numOnes
        return numOnes-remainder
        