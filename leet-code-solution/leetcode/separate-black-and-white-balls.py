class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        sol = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                count += 1
            else:
                sol += count
        return sol
        