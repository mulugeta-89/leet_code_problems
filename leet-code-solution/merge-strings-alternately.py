class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = len(word1), len(word2)
        c = min(a,b)
        sol = ""
        for i in range(c):
            sol += word1[i]
            sol += word2[i]
        if c < a:
            sol += word1[c:]
        if c < b:
            sol += word2[c:]
        return sol