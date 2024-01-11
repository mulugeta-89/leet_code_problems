class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        left = 0
        sol = 0
        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[right])
            sol = max(sol, right-left+1)
        return sol