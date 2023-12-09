class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sol_s = ""
        count = 0
        for i in range(len(s)):
            if count < len(spaces) and i == spaces[count]:
                sol_s +=  " "
                count += 1
            sol_s += s[i]
        return sol_s
        