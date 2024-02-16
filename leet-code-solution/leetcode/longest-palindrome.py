class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = {}
        length = 0
        for item in s:
            if item in s_dict:
                s_dict[item] += 1
                if s_dict[item] % 2 == 0:
                    length += 2
            else:
                s_dict[item] = 1
        return length + 1 if len(s) != length else length
        