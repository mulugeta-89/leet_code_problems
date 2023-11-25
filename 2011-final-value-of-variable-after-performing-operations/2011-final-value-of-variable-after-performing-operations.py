class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sol = 0
        for item in operations:
            if item == "++X" or item == "X++":
                sol += 1
            else:
                sol -= 1
        return sol
        