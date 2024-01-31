class Solution:
    def balancedString(self, s: str) -> int:
        freq = {
        "W":0,
        "Q":0,
        "R":0,
        "E":0
    }
        for i in range(len(s)):
            freq[s[i]] += 1
        left = 0
        count = len(s)/4
        mini = float("inf")
        for right in range(len(s)):
            freq[s[right]] -= 1
            while left < len(s) and freq["E"] <= count and freq["Q"] <= count and freq["R"] <= count and freq["W"] <= count:
                mini = min(mini, right-left+1)
                freq[s[left]] += 1
                left += 1
        return mini
        