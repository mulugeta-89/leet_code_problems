class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        r = len(s)-1
        steps = 0
        while l < r:
            if s[l] == "1" and s[r] == "0":
                steps += (r-l)
                l += 1
                r -= 1
            if s[l] == "0":
                l += 1
            if s[r] == "1":
                r -= 1
        return steps
        
        